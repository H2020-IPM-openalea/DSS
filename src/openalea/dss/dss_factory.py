"""A module that allow exporting an openalea node/factory as an IPM model"""
import json
import inspect

def oa_type(interface):
    """Openalea.core interface, without the I and lowercase"""
    return str(interface)[1:].lower()

# mapping of openalea types to pydantic (python) types
def py_type(oa_type):
    py_types = {'sequence': 'list',
                'filestr': 'str',
                'dirstr': 'str',
                'textstr': 'str',
                'codestr': 'str',
                }
    return py_types.get(oa_type, oa_type)

# mapping of py_types to json schema types
json_type={'str': 'string',
              'float': 'number',
              'int': 'integer',
              'dict': 'object',
              'list': 'array',
               'tuple': 'array',
              'bool': 'boolean',
              None: 'null'}

#mappping of json types to pydantic types
pydantic_type={'string': 'str',
              'number': 'float',
              'integer': 'int',
              'object': 'dict',
              'array': 'list',
              'boolean': 'bool',
              'null': None}



pydantic_parameter_template="""
    {name}: {type}"""

pydantic_template="""from __future__ import annotations

from typing import List

from pydantic import BaseModel


class ConfigParameters(BaseModel):{config_params}


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


class PydanticModel(BaseModel):
    modelId: str
    configParameters: ConfigParameters
    weatherData: WeatherData
"""

fastAPI_template="""{pydantic_model}

from fastapi import FastAPI
from openalea.dss.dss_factory import encode_input

app = FastAPI()

from openalea.core.node import FuncNode
from openalea.core import IFloat, IInt

{model_source}

inputs = {inputs}
outputs = {outputs}
node = FuncNode(inputs, outputs, {model_name})
node.name='{model_id}'


input_mapping = {input_mapping}

@app.post("/{model_id}/")
async def model_evaluation(data: PydanticModel):
    input_data = data.dict()
    inputs = encode_input(node, input_data, input_mapping)
    return [node(input) for input in inputs]
"""

fake_input_data = """{
  "modelId": "TRISK",
  "configParameters": {
    "timeStart": "2020-05-01",
    "timeEnd": "2020-05-03",
    "threshold": 15
  },
  "weatherData": {
    "timeStart": "2020-04-30T22:00:00Z",
    "timeEnd": "2020-05-02T22:00:00Z",
    "interval": 86400,
    "weatherParameters": [
        1002
    ],
    "locationWeatherData": [
        {
            "longitude": 10.781989,
            "latitude": 59.660468,
            "altitude": 94.0,
            "data": [
                [
                    5.7
                ],
                [
                    8.2
                ],
                [
                    8.5
                ]
            ],
            "length": 3,
            "width": 1
        }
    ]
  }
}
"""
def encode_input(node, input_data, input_mapping):
    inputs={}
    length = input_data['weatherData']['locationWeatherData'][0]['length']
    for p in input_mapping['config_params']:
        inputs[p] = [input_data['configParameters'].get(p,0)] * length
    wdata = dict(zip(input_data['weatherData']['weatherParameters'],zip(*input_data['weatherData']['locationWeatherData'][0]['data'])))
    for p, p_code in input_mapping['weather_parameters'].items():
        inputs[p] = wdata[p_code]
    return list(zip(*[inputs[port['name']] for port in node.input_desc]))



def wrap_inputs(node, parameters):
    inputs={}
    node_ports = {port['name']: port for port in node.input_desc}
    for p in parameters:
        port = node_ports[p]
        d = dict(default=port['value'])
        oat = oa_type(port['interface'])
        if oat == 'datetime':
            d['format'] = 'date-time'
        d['type'] = json_type[py_type(oat)]
        inputs[p] = d
    return inputs


def wrap_outputs(node, decision_support=None):
    if decision_support is None:
        decision_support = 'None'
    def _ipm_port(port):
        return dict(id=port['name'])

    output = dict(warning_status_interpretation =decision_support,
                result_parameters = [_ipm_port(p) for p in node.output_desc])
    return output


def dss_factory(node, interval=86400, weather_parameters=None, parameters=None, decision_support=None, template=None):
    """Transform an openalea node in a IPM model json descriptor and generate a fastAPI script to launch webservice

    Args:
        node: the node to be exported
        interval: the time step of the model (s)
        weather_parameters: a mapping between node input name and weather data codes, if any.
        None if none of the input is a weather data
        parameters: a list of node input name to be exposed as config parameters in IPM-Decison platform
        template: (optional) an existing IPM model to be used as a template for filling missing information
    Returns:
        model: a json-like dict describing the model
        dss_service: a string containing the script to be run for launching the web service

    """
    model = template._model.copy()
    model_id = node.name
    model['id'] = model_id
    model['execution']['endpoint'] = f'http://127.0.0.1:8000/{model_id}/'

    if weather_parameters is None:
        model['input']['weather_parameters'] = None
    else:
        model['input']['weather_parameters'] = [{'parameter_code': v, 'interval': interval} for v in weather_parameters.values()]

    properties = model['execution']['input_schema']['properties']
    properties['modelId']['pattern'] = '^%s$'%(model_id)
    properties['modelId']['default'] = model_id
    properties['modelId']['description'] = 'Must be %s'%(model_id)

    config = properties['configParameters']['properties']
    if weather_parameters is None:
        config = {}
    else:
        config = {k:v for k,v in config.items() if k in ('timeStart', 'timeEnd')}
    if parameters is not None:
        inputs = wrap_inputs(node, parameters)
        config.update(inputs)
    properties['configParameters']['properties'] = config
    properties['configParameters']['required'] = list(config.keys())
    model['execution']['input_schema']['required'] = ['modelId', 'configParameters']
    model['output'] = wrap_outputs(node, decision_support=decision_support)


    config_params = ''.join([pydantic_parameter_template.format(name=k, type=pydantic_type[v['type']]) for k,v in config.items()])
    pydantic_model = pydantic_template.format(config_params=config_params)
    input_mapping = "{'weather_parameters': %s, 'config_params': %s}"%(json.dumps(weather_parameters),json.dumps(parameters))
    dss_service = fastAPI_template.format(model_source=inspect.getsource(node.func),
                                          model_name= node.func.__name__,
                                          pydantic_model=pydantic_model,
                                          model_id=model_id,
                                          input_mapping=input_mapping,
                                          inputs=node.input_desc,
                                          outputs=node.output_desc)
    return model, dss_service