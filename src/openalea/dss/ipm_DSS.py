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
            df=df[["pests","crops","description","input","output"]]
            df=pandas.concat([df.drop("description",axis=1),df['description'].apply(pandas.Series)],axis=1)
            df.rename(columns={'other':'description'}, inplace=True)
            df=df.drop(['created_by', 'age', 'assumptions', 'peer_review', 'case_studies'],axis=1)
            
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
        
        
        d={dss:[model for model in h.catalog[dss]] for dss in h.catalog} # dict with dss:model
        
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
    
    @property    
    def information(self):
        """ Return information of the model

        Returns
        -------
        dict
            dict containing model information 
        """
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
        
        output_result = {key: data[key] for key in [item["id"] for item in self.information["output"]["result_parameters"]]}
        #data['warningStatus']=output['locationResult'][0]['warningStatus']
        
        times_index= pandas.date_range(start=output['timeStart'], end=output['timeEnd'], freq=str(output['interval'])+"s")
        
        df=pandas.DataFrame(output_result, index=times_index.values)
        
        # convert dataframe to xarray dataset
        ds = xr.Dataset.from_dataframe(df)
        ds = ds.rename({'index':'time'})
        
        # add attribut
        ds.time.attrs["name"]="time"
        ds.time.attrs["units"]="days"
        
        #variable attributs
        source = self.information

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
        attrs['description']=source['description']["other"]
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
        output.to_dataframe().plot.line()
        plt.ylabel(self.information["output"]['chart_heading'])
        plt.title(self.information["output"]['chart_heading'])
        plt.suptitle(output.name)      