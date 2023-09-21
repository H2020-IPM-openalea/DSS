from __future__ import annotations
from fastapi import FastAPI
from openalea.dss.dss_factory import encode_input
#from json_to_pydantic import json_to_pydantic,jsontext


#from agroservices.ipm.ipm import IPM
#import agroservices.ipm.fakers as fakers
#ipm = IPM()
#model = ipm.get_model(DSSId='no.nibio.vips',ModelId='PSILARTEMP')
#input_data = fakers.input_data(model)

#json_to_pydantic(json.dumps(input_data))


#import pydantic_input_model

#hack_import_node (to be done with package manager)
from openalea.core.node import FuncNode
from openalea.core import IFloat, IInt
def t_risk(tair, threshold=15):
    if tair <= threshold:
        return 0
    else:
        return 1
inputs = (dict(name='tair', interface=IFloat, value=None),
          dict(name='threshold', interface=IFloat, value=15))
outputs = (dict(name='Risk', interface=IInt), )
node = FuncNode(inputs, outputs, t_risk)
node.name='TRISK'
# end hack



input_mapping = {'weather_parameters': {"tair": 1002}, 'config_params': ["threshold"]}


from typing import List

from pydantic import BaseModel


class ConfigParameters(BaseModel):
    timeZone: str
    timeStart: str
    timeEnd: str


class LocationWeatherDatum(BaseModel):
    longitude: float
    latitude: float
    altitude: float
    data: List[List[float]]
    length: int
    width: int


class WeatherData(BaseModel):
    timeStart: str
    timeEnd: str
    interval: int
    weatherParameters: List[int]
    locationWeatherData: List[LocationWeatherDatum]


class Model(BaseModel):
    modelId: str
    configParameters: ConfigParameters
    weatherData: WeatherData

app = FastAPI()


@app.post("/items/")
async def create_item(item: Model):
    input_data = item.dict()
    inputs = encode_input(node, input_data, input_mapping)
    return [node(args) for args in inputs]