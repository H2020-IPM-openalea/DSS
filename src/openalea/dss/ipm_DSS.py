# -*- python -*-
# -*- coding:utf-8 -*-
#
#       Copyright 2020 INRAE-CIRAD
#       Distributed under the Cecill-C License.
#       See https://cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
# ==============================================================================

import pandas
import json
import xarray as xr

from agroservices import IPM
from weatherdata import WeatherDataHub

class Model:
    """[summary]
    """
    def __init__(self, dss, model):
        """[summary]

        Parameters
        ----------
        dss : [type]
            [description]
        model : [type]
            [description]
        """
        self.pkg = self.dss = dss
        self.name = model
        self.ipm_hub = IPM()
        self.ws = WeatherDataHub()
    
    @property
    def information(self):
        return self.ipm_hub.get_model(ModelId=self.dss, DSSId=self.name)
    
    model_information = information
    
    def input_DSS_weather_model_json(
        self,
        timeZone ="UTC",
        TimeStart ="2020-05-01",
        TimeEnd ="2020-05-03",
        weatherDataService='Finnish Meteorological Institute measured data',
        parameters=[1002],
        stationId=[101104]):
        """
        Create an json input weather data for model
        
        Parameters
        ----------
            timeZone:(txt) Timezone of climatic data (eg:"UTC", Europe/Oslo)
            TimeStart: (double) start date for meteological data
            TimeEnd: (double) end date for meteological data
            weatherDataService:(txt, name of weather data service) Weather data service present in IPM plateform (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)
            parameters:(list of int) Meteorological parameters code (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)
            station_id: (int)nid of meterological station. (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)

        Returns
        --------
            input weather data for the model (json file)
        """
        d= {
        "modelId": self.DSSId,
        "configParameters": {
            "timeZone": timeZone,
            "timeStart": TimeStart,
            "timeEnd": TimeEnd
        },
        "weatherData": self.ws.get_ressource(name=weatherDataService).data(
            parameters=parameters,
            stationId=stationId,
            timeStart=TimeStart,
            timeEnd=TimeEnd,
            timeZone=timeZone,
            format='json')[0]
        }
        
        with open('model_input_weatherdata.json', 'w') as outfile:
            json.dump(d, outfile)
            
        return d

    def input_DSS_fieldobservation_model_json(
        self,
        timeZone ="UTC",
        TimeStart ="2020-05-01",
        TimeEnd ="2020-05-03",
        fieldobservation='fieldobservation.json'):
        """
        Create an json input field observation data for model
        
        Parameter
        ----------
            timeZone:(txt) Timezone of climatic data (eg:"UTC", Europe/Oslo)
            TimeStart: (double) start date for meteological data
            TimeEnd: (double) end date for meteological data

        Returns
        --------
            input data for the model (json file)
        """

        d= {
        "modelId": self.DSSId,
        "configParameters": {
            "timeZone": timeZone,
            "startDateCalculation": TimeStart,
            "endDateCalculation": TimeEnd}
        }
        
        with open(fieldobservation) as json_file:
            data = json.load(json_file)
        
        d['configParameters'].update(data)

        with open('model_input_fieldobservation.json', 'w') as outfile:
            json.dump(d, outfile)
        return d
    
    def run(
        self,
        modelInput="model_input.json"):
        """
        Get data of the model

        Parameters:
        -----------
            model_input: json file obtain with input_model_json function
        
        Returns:
        --------
            A dataframe containing output of the model
        """
        
        rep= self.ipm.run_model(
            ModelId=self.ModelId,
            DSSId=self.DSSId,
            model_input=modelInput)
        
        # add a new method that converts an output into an xarray
        # _output2xarray
        data = {str(var): vals for var, vals in zip(rep['resultParameters'], zip(*rep['locationResult'][0]['data']))}
        data['warningStatus']=rep['locationResult'][0]['warningStatus']
        
        times_index= pandas.date_range(start=rep['timeStart'], end=rep['timeEnd'], freq=str(rep['interval'])+"s")
        df=pandas.DataFrame(data, index=times_index.values)
        
        # convert dataframe to xarray dataset
        ds = xr.Dataset.from_dataframe(df)
        ds = ds.rename({'index':'time'})
        
       
        # index attributs
        ds.time.attrs["name"]="time"
        ds.time.attrs["units"]="days"
        
        #variable attributs
        source = self.model_information()
        
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
    
    get_data_model = run
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.run(*args, **kwds)
    
    # add a __repr__ and __str__ method
class DSSHub(object):
    def __init__(self):
        self.ipm = IPM()
    
    def list_dss(self, ViewDataFrame=False):
        """
        Get a dict of available DSS on the IPM catalog, modelsid, name, and description

        Parameters
        -----------
        
        Returns
        --------
            dictionnary or Dataframe with DSSid, ModelId, name ,description and endpoint for each ModelID
        """
        rep= self.ipm.get_dss()
        d= {el['id']:{el['models'][item]['id']:{"name":el['models'][item]['name'],"description":el['models'][item]['description'],'endpoint':el['models'][item]['execution']['endpoint']}  for item in range(len(el['models']))} for el in rep}

        if ViewDataFrame == False:
            return d
        else:
            df = pandas.Series(d).apply(pandas.Series).stack().reset_index()
            df.columns=["Modelid","DSSid",'0']
            df=pandas.concat([df.drop(['0'], axis=1), df['0'].apply(pandas.Series)], axis=1)
            return df
    
    def get_dss(self,ModelId='no.nibio.vips',DSSId='PSILARTEMP'):
        """
        Get DSS model

        Parameters
        -----------
            ModelID: (str) id of the model (eg:'no.nibio.vips')
            DSSId: (str) id of the dds (eg: PSILARTEMP)
        
        Returns
        --------
            DSSdata class of the modelid and dssid
        """
        rep= self.ipm.get_dss()

        modelid= [el['id'] for el in rep]
        dssid=[[el['models'][item]['id'] for item in range(len(el['models']))]for el in rep]

        if (ModelId in modelid and DSSId in dssid[item] for item in range(len(dssid))):
            return DSSdata(ModelId,DSSId)
        else:
            raise NotImplementedError()

# retrocompatibility : refactoring
DSSHub = Hub 
DSSdata = Model 


