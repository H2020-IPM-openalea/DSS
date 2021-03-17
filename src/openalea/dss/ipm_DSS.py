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
from agroservices import IPM
from weatherdata import WeatherDataHub

class DSSdata(object):
    
    def __init__(self, ModelId, DSSId):
        self.ModelId = ModelId
        self.DSSId = DSSId
        self.ipm = IPM()
        self.ws = WeatherDataHub()
        
    def input_DSS_weather_model_json(
        self,
        timeZone ="UTC",
        TimeStart ="2020-05-01",
        TimeEnd ="2020-05-03",
        weatherDataService='Finnish Meteorological Institute measured data',
        parameters=[1002],
        station_id=101104):
        """
        Create an json input weather data for model
        
        Parameter:
        ----------
            timeZone:(txt) Timezone of climatic data (eg:"UTC", Europe/Oslo)
            TimeStart: (double) start date for meteological data
            TimeEnd: (double) end date for meteological data
            weatherDataService:(txt, name of weather data service) Weather data service present in IPM plateform (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)
            parameters:(list of int) Meteorological parameters code (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)
            station_id: (int)nid of meterological station. (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)

        Returns:
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
        "weatherData": self.ws.get_ressource(name=weatherDataService).get_data(
            parameters=parameters,
            station_id=station_id,
            timeStart=TimeStart,
            timeEnd=TimeEnd,
            timezone=timeZone,
            ViewDataFrame=False)
        }
        
        with open('model_input_weatherdata.json', 'w') as outfile:
            json.dump(d, outfile)

    def input_DSS_fieldobservation_model_json(
        self,
        timeZone ="UTC",
        TimeStart ="2020-05-01",
        TimeEnd ="2020-05-03",
        weatherDataService='Finnish Meteorological Institute measured data',
        parameters=[1002],
        station_id=101104):
        """
        Create an json input field observation data for model
        
        Parameter:
        ----------
            timeZone:(txt) Timezone of climatic data (eg:"UTC", Europe/Oslo)
            TimeStart: (double) start date for meteological data
            TimeEnd: (double) end date for meteological data
            weatherDataService:(txt, name of weather data service) Weather data service present in IPM plateform (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)
            parameters:(list of int) Meteorological parameters code (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)
            station_id: (int)nid of meterological station. (see:https://ipmdecisions.nibio.no/api/wx/apidocs/)

        Returns:
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
        
        with open('fieldobservation.json') as json_file:
            data = json.load(json_file)
        
        d['configParameters'].update(data)

        with open('model_input_fieldobservation.json', 'w') as outfile:
            json.dump(d, outfile)

    def get_data_model(
        self,
        model_input="model_input.json"):
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
            model_input=model_input)
        
        d = {str(var): vals for var, vals in zip(rep['resultParameters'], zip(*rep['locationResult'][0]['data']))}
        dt=rep['locationResult'][0]['warningStatus']
        
        df1=pandas.DataFrame(d)
        df2= pandas.DataFrame(dt)
        df2.columns=['warningStatus']

        df=pandas.DataFrame.merge(df1,df2, left_index=True,right_index=True)

        return df

class DSSHub(object):
    def __init__(self):
        self.ipm = IPM()
    
    def list_dss(self, ViewDataFrame=False):
        """
        Get a dict of available DSS on the IPM catalog, modelsid, name, and description

        Parameters:
        -----------
        
        Returns:
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

        Parameters:
        -----------
            ModelID: (str) id of the model (eg:'no.nibio.vips')
            DSSId: (str) id of the dds (eg: PSILARTEMP)
        
        Returns:
        --------
            DSSdata class of the modelid and dssid
        """
        rep= self.ipm.get_dss()

        modelid= [el['id'] for el in rep]
        dssid=[[el['models'][item]['id'] for item in range(len(el['models']))]for el in rep]

        if (ModelId in modelid and DSSId in dssid[0]):
            return DSSdata(ModelId,DSSId)
        else:
            raise NotImplementedError()





