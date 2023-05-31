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

def patch_call(instance, func, doc):
    class _(type(instance)):
        def __call__(self, *arg, **kwarg):
           return func(*arg, **kwarg)
    instance.__class__ = _
    instance.__call__.__func__.__doc__ = doc

class DSS(object):
    def __init__(self, name, meta, models, manager):
        self.name = name
        self.meta = meta
        self.models=models
        self._dssm = manager

    @property
    def name_(self):
        return '_'.join(self.name.split('.'))

    def as_package(self):
        org = self.meta['organization']
        institute = ', '.join([org['name'],org['address'], org['postal_code'], org['city'], org['country']])

        metainfo=dict(
            license='unknown',
            version=self.meta['version'],
            authors=', '.join([org['email'], org['url']]),
            institutes=institute,
            url=self.meta['url'],
            description=self.meta['name']
        )

        package_dict = {k: self.get(k).as_node() for k,v in self.models.items()}

        package = dict(name=self.name_,
                       metainfo=metainfo,
                       package_dict=package_dict)
        return package

    def get(self,  model_name="PSILARTEMP"):
        """[Get model]

        Parameters
        ----------
        dss : str, optional
            [description], by default "no.nibio.vips"
        model : str, optional
            [description], by default "PSILARTEMP"
        """

        if model_name in self.models:
             model = Model(self.models[model_name], self.name, self._dssm)

             def _model_call(*args, **kwargs):
                 return kwargs
             patch_call(model, _model_call, 'test_doc')
             return model
        else:
            raise ValueError('Model ' + model_name + ' not found in ' + self.name)
class Model(object):
    """ Model Class derived from Hub. It allows to displays informations and run model and plot output

    Parameters
    ----------
    Hub : class
        Class allows to access IPM catalog and get one model
    """
    
    def __init__(self, model, dss, manager):
        """Init of Model class model

        Parameters
        ----------_
        dss : str
            id of the dss
        model : str
            id of the model
        """
        self._model = model
        self.dss = dss
        self._dssm = manager
        self._parameters = {p['id'] : p for p in self._dssm._ipm.get_parameter()}

    @property
    def model_id(self):
        return self._model['id']
    @property
    def model(self):
        return self._model['name']

    @property
    def meta(self):
        return {k: v for k, v in self._model.items() if k not in ['input', 'output', 'execution']}

    @property
    def inputs(self):
        inputm = {'parameters': {},
                 'weather_data': {},
                 'field_observations': {}}

        _input_schema = self._model['execution']['input_schema'].copy()
        _input = self._model['input'].copy()
        for k in ('modelId', 'weatherData', 'fieldObservations'):
            if k in _input_schema['properties']:
                _input_schema['properties'].pop(k)

        for p in _input_schema['properties'].values():
            if isinstance(p, dict):
                if 'properties' in p:
                    inputm['parameters'].update(p['properties'])
                else:
                    inputm['parameters'].update(p)

        if _input['weather_parameters'] is not None:
            wp = _input['weather_parameters']
            parameters = [elt['parameter_code'] for elt in wp]
            inputm['weather_data'].update({p: self._parameters[p] for p in parameters})

            # filter parameters that are used internaly to query weather data
            for w in ('weather_data_period_start', 'weather_data_period_end'):
                items = {item['determined_by']: item['value']
                            for item in _input[w]}
                if 'INPUT_SCHEMA_PROPERTY' in items:
                    fields = items['INPUT_SCHEMA_PROPERTY'].split('.')
                    if len(fields) > 1:
                        name = fields[-1]
                        if name in inputm['parameters']:
                            inputm['parameters'].pop(name)

        if _input['field_observation'] is not None:
            for w in ('fieldObservations', 'fieldObservationQuantifications'):
                if w in inputm['parameters']:
                    inputm['parameters'].pop(w)
            observations = next(iter(_input_schema['definitions'].values()))
            inputm['field_observations'] = observations['properties']

        return inputm

    @property
    def outputs(self):
        return [{k:v for k,v in d.items() if k != 'chart_info'} for d in self._model['output']['result_parameters']]

    def as_node(self):
        """Construct inputs of an Openalea node representing the model"""

        inputs = []
        for p, v in self.inputs['weather_data'].items():
            dp = {}
            dp['name'] = p
            dp['description'] = v['name']
            dp['interface'] = 'Ifloat'
            inputs.append(dp)

        for p, v in self.inputs['field_observations'].items():
            dp = {}
            dp['name'] = p
            dp['description'] = v['title']
            dp['interface'] = 'I' + v.get('type', 'float')
            inputs.append(dp)

        for p,v in self.inputs['parameters'].items():
            dp = {}
            dp['name'] = p
            dp['description'] = v.get('title', None)
            dp['interface'] = v.get('type', None)
            dp['value'] = v.get('default', None)
            inputs.append(dp)

        outputs=[]
        for item in self.outputs:
            dp={}
            dp['name'] = item['id']
            dp['description'] = item['title']
            outputs.append(dp)

        node = dict(
            name=self.meta['id'],
            category='DSS',
            description=self.meta['name'],
            inputs=inputs,
            outputs=outputs,
            nodemodule='_'.join(self.dss.split('.')) + '.py',
            nodeclass='_'.join(self.dss.split('.')) + '_' + self.model_id,
            authors=self.meta['authors']
        )
        return node

    def informations(self,display=None):
        """ Return information of the model

        Returns
        -------
        dict
            dict containing model information 
        """
        inf=self._model
        
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
            return self._model
    
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
    
    def run(self, weatherdata=None, fieldObservation=None,view="ds"):
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
                return d
                
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
                    return field_observation_input

        output= self._dssm._ipm.run_model(self._model,
                                    input_data= input(weatherdata=weatherdata,fieldObservation=fieldObservation))
        
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
        """
        Reader dataframe for field observations.It must contain:
        Date of observation: start Date of experiment, End date experiment and date of Observation
        
        Parameters
        ----------
        path : str, optional
            field observation datafile path,
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
        """
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