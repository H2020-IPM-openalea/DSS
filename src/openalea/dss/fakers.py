"""Faker classes"""
import random
import agroservices.ipm.fakers as agro_fakers
from weatherdata.converters import weather_data_as_xarray

class WeatherDataSource(object):


    def data(self,
             parameters=None,
             stationId =None,
             timeStart = None,
             timeEnd = None,
             timeZone = None,
             altitude = None,
             longitude = None,
             latitude = None,
             interval = 3600,
             length=3):
        weather_data = agro_fakers.weather_data(parameters=parameters,
                                   interval=interval,
                                   longitude=longitude,
                                   latitude=latitude,
                                   altitude=altitude,
                                   length=length)
        return weather_data_as_xarray(weather_data)

def node_inputs(model):
    fake={}
    for ptype in model.inputs:
        for p in model.inputs[ptype]:
            fake[p]=model.inputs[ptype][p].get('default', random.uniform(0,20))
    return fake
