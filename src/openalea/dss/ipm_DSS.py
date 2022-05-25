# -*- python -*-
# -*- coding:utf-8 -*-
#
#       Copyright 2020 INRAE-CIRAD
#       Distributed under the Cecill-C License.
#       See https://cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
# ==============================================================================

import pandas
import numpy as np
import json
import xarray as xr
import matplotlib.pyplot as plt
from agroservices import IPM

class Hub:
    """Class Hub
    
    Hub allows to access IPM catalog and get one model. 
    """
    
    def __init__(self):
        """[summary]
        """
        self.ipm_hub=IPM()
        self._catalog = None
    
    @property 
    def catalog(self):
        """ Trasform ipm catalogue from agroservices request in dict

        Returns
        -------
        [dict]
            [dict of dss catalog with meta-information by dss and model]
        """
        if self._catalog is None:
            self._catalog = self.ipm_hub.get_dss()
           
        return  {el["id"]: {item["id"]:item for item in el["models"]} for el in self._catalog}
    
    
    def display(self,view="dataframe"):
        """Display catalog meta information (dss, model and description)

        Parameters
        ----------
        view : str, optional
            [choose the type of catalog visualisation dataframe or dict], by default "dataframe"

        Returns
        -------
        [dataframe or dict]
            [return a dataframe or a dict]
        """
        if view=="dataframe":
            df=pandas.Series(self.catalog).apply(pandas.Series).stack().apply(pandas.Series)
            df=df[["pests","crops","description"]]
            # df=pandas.concat([df.drop("description",axis=1),df['description'].apply(pandas.Series)],axis=1)
            # df.rename(columns={'other':'description'}, inplace=True)
            # df=df.drop(['created_by', 'age', 'assumptions', 'peer_review', 'case_studies'],axis=1)
            df=df.reset_index()
            df.rename(columns={"level_0":"dss","level_1":"models"},inplace=True)
            
            return df
        
        else:
            print(self.catalog)
    
    def get(self, dss="no.nibio.vips", model="PSILARTEMP"):
        """[Get model]

        Parameters
        ----------
        dss : str, optional
            [description], by default "no.nibio.vips"
        model : str, optional
            [description], by default "PSILARTEMP"
        """
        
        
        d={dss:[model for model in self.catalog[dss]] for dss in self.catalog} # dict with dss:model
        
        if (dss in d and model in d[dss]):
            return Model(dss,model)
        else:
            raise NotImplementedError()
        

class Model(Hub):
    """ Model Class derived from Hub. It allows to displays informations and run model and plot output

    Parameters
    ----------
    Hub : class
        Class allows to access IPM catalog and get one model
    """
    
    def __init__(self, dss, model):
        """Init of Model class model

        Parameters
        ----------
        dss : str
            id of the dss
        model : str
            id of the model
        """
        self.dss=dss
        self.model=model
        Hub.__init__(self)
    
       
    def informations(self,display=None):
        """ Return information of the model

        Returns
        -------
        dict
            dict containing model information 
        """
        inf=self.catalog[self.dss][self.model]
        
        if display=="dataframe":
            d=dict()
            for (key,value) in inf.items():
                if key in ['name', 'id', 'version', 'type_of_decision']:
                    d[key]=value
                if key in ['pests', 'crops']:
                    d[key]= value
                if key=="description":
                    d[key]=value
                if key=="input":
                    if value["weather_parameters"] is not None:
                        d["weather input"]= ", ".join([str(el["parameter_code"]) for el in value["weather_parameters"]])
                    else:
                        d["weather input"]= None
                    
                    if value["field_observation"] is not None:
                        d["field_observation input"]= json.loads(inf["execution"]["input_schema"])["definitions"]["fieldObs_PSILRO"]["required"]
                    else:
                        d["field_observation input"]=None
                if key == "output":
                    d[key]=", ".join([el["id"] for el in value["result_parameters"]])
                    d["output_description"]=", ".join([el["title"] for el in value["result_parameters"]])
                  

            df=pandas.Series(d).to_frame().T
            df=df[["name","id",'description',"type_of_decision","pests","crops","weather input","field_observation input","output","output_description"]]
            return df
        else:        
            return self.catalog[self.dss][self.model]
    
    def __xarray_convert__(self, output):
        """ Convert model output of the model in xarray dataset 

        Parameters
        ----------
        output : dict
            output of (run) model 

        Returns
        -------
        xarray.Dataset
            return a xarray.Dataset containing output of model with meta-information (attribut)
        """
        
        data = {str(var): vals for var, vals in zip(output['resultParameters'], zip(*output['locationResult'][0]['data']))}
        data['warningStatus']=output['locationResult'][0]['warningStatus']
        output_result = {key: data[key] for key in [item["id"] for item in self.informations()["output"]["result_parameters"]]}
        
        
        times_index= pandas.date_range(start=output['timeStart'], end=output['timeEnd'], freq=str(output['interval'])+"s")
        
        df=pandas.DataFrame(output_result, index=times_index.values)
        
        # convert dataframe to xarray dataset
        ds = xr.Dataset.from_dataframe(df)
        ds = ds.rename({'index':'time'})
        
        # add attribut
        ds.time.attrs["name"]="time"
        ds.time.attrs["units"]="days"
        
        #variable attributs
        source = self.informations()

        data_vars_attrs={el['id']:{key:el[key] for key in ['title','description']} for el in source['output']['result_parameters']}

        for el in list(ds.data_vars):
            if el in list(data_vars_attrs):
                ds.data_vars[el].attrs=data_vars_attrs[el]
                
        # dataset attribut
        attrs={}
        attrs['name']=source['name']
        attrs['id']=source['id']
        attrs['version']=source['version']
        attrs['authors']=source['authors'][0]
        attrs['description']=source['description']
        attrs['description_url']=source['description_URL']

        ds.attrs = attrs
        
        return ds
    
    def run(self,weatherdata=None,fieldObservation=None,view="ds"):
        """ Run model

        Parameters
        ----------
        weatherdata : object, optional
            list of json containing weather data information from ipm weatherdata service, by default None
        fieldObservation : object, optional
            json object containing field observation, by default None
        view : str, optional
            parameter controlling the type of output (xarray.Dataset or json), by default "ds"
        """
        
        def input(weatherdata=None, fieldObservation=None):
            """ Fonction to create input data model according to IPM format

            Parameters
            ----------
            weatherdata : Object JSON, optional
                weatherdata from weather data ipm services in json format, by default None
            fieldObservation : Object JSON, optional
                field observation data in json format according IPM format, by default None

            Returns
            -------
            Object JSON
                return input json object to run model
            """
            
            if weatherdata is not None:
                fieldObservation=None                                
                d= {"modelId": self.model,
                    "configParameters": {
                        "timeZone": "UTC",
                        "timeStart": weatherdata[0]["timeStart"],
                        "timeEnd": weatherdata[0]["timeStart"]
                        },
                    "weatherData": weatherdata[0]
                }
                return json.dumps(d)
                
            else: 
                if type(fieldObservation) is pandas.DataFrame:
                    
                    json_obs={"fieldObservations":
                        [
                            {"location":
                                {"type":"Point",
                                "coordinates":fieldObservation.attrs["location"]["coordinates"]
                                },
                                "time":fieldObservation.attrs["time"],
                                "pestEPPOCode":fieldObservation.attrs["pestEPPOCode"],
                                "cropEPPOCode":fieldObservation.attrs["cropEPPOCode"]
                                }
                        ],
                        "fieldObservationQuantifications":
                            [
                                {"trapCountCropEdge":int(fieldObservation.trapCountCropEdge.dropna().values),
                                "trapCountCropInside":int(fieldObservation.trapCountCropInside.dropna().values)
                                }
                            ]
                        }
                            
                    
                    field_observation_input={
                        "modelId":self.model,
                        "configParameters":
                            {"timeZone": fieldObservation.index.tz._tzname,
                            "startDateCalculation":np.datetime_as_string(pandas.Timestamp.to_datetime64(fieldObservation.index[0]), unit='D'),
                            "endDateCalculation":np.datetime_as_string(pandas.Timestamp.to_datetime64(fieldObservation.index[-1]), unit='D')
                            }
                        }
                    
                    field_observation_input["configParameters"].update(json_obs)
                    return json.dumps(field_observation_input)
                      
        output= self.ipm_hub.run_model(ModelId=self.dss,
            DSSId=self.model,
            model_input= input(weatherdata=weatherdata,fieldObservation=fieldObservation))
        
        if view== "ds":
            return self.__xarray_convert__(output=output)
        else:
            return output
    
    def plot(self,output):
        """Plot output result

        Parameters
        ----------
        output : xarray.Dataset
            Return a plot from output model conform to the description of output information of the model 
        """
        output.fillna(0).to_dataframe().plot.line()
        plt.ylabel(self.informations()["output"]['chart_groups'][0]["title"])
        plt.suptitle(output.name)      
        
    def df_reader_fieldObservation(self,path,
                               longitude,
                               latitude,
                               timeZone,
                               sep,
                               dayfirst,
                               pestEPPOCode,
                               cropEPPOCode,
                               convert_name=None):
        r'''
        Reader dataframe for field observations.It must contains:
        Date of observation: start Date of experiment, End date experiment and date of Observation

        Parameters
        ----------
        path : str, optional
            field observation datafile path, by default r'C:\Users\mlabadie\Documents\GitHub\dss\example\psilarobs.csv'
        longitude : float, optional
            longitude in degree of experimental site, by default 11.025635
        latitude : float, optional
            latitude in degree of experimental site, by default 59.715791
        timeZone : str, optional
            timezone of experimental site, by default "Europe/Paris"
        sep : str, optional
            separator of file, by default ";"
        dayfirst : bool, optional
            if date begin by time True else False, by default True
        PestEPPOCode: str
            pestEPPOCode of the model selected here SEPTAP
        cropEPPOCode: str
            cropEPPOCode of the model selected here APUGD

        Returns
        -------
        pandas.Dataframe
            return a dataframe with attribute information need to compute observation file input
        '''
        data=pandas.read_csv(path,sep=sep)
        time=pandas.to_datetime(data["time"],dayfirst=dayfirst).tolist()
        data.index=pandas.date_range(start=time[0],end=time[-1],tz=timeZone)    
        data=data.drop(columns="time")
        data.attrs={"time":np.datetime_as_string(data.dropna().index.tz_convert("UTC").values[0],timezone='UTC',unit="m"),"location":{"type":"Point","coordinates":[str(longitude), str(latitude)]},"pestEPPOCode":pestEPPOCode,"cropEPPOCode":cropEPPOCode}
        if convert_name is not None:
            data=data.rename(convert_name)
        else:
            data=data
        return data