"""A module that allow exporting an openalea node/factory as an IPM model"""
import json

fastAPI_template="""from fastapi import FastAPI
from openalea.dss.dss_factory import encode_input

app = FastAPI()

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

input_mapping = {input_mapping}

@app.post("/dss/model/{dss_name}/{model_id}/")
async def model_evaluation(input_data):
    inputs = encode_input(node, input_data, input_mapping)
    return ','.join([str(node(input)) for input in inputs])
"""

fake_input_data = """{
  "modelId": "TRISK",
  "configParameters": {
    "threshold": 15,
    "timeStart": "2020-05-01",
    "timeEnd": "2020-05-03"
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
        inputs[p] = [input_data['configParameters'].get(p)] * length
    wdata = dict(zip(input_data['weatherData']['weatherParameters'],zip(*input_data['weatherData']['locationWeatherData'][0]['data'])))
    for p, p_code in input_mapping['weather_parameters'].items():
        inputs[p] = wdata[p_code]
    return list(zip(*[inputs[port['name']] for port in node.input_desc]))


def _type(interface):
    return str(interface)[1:].lower()

def wrap_inputs(node, parameters):
    inputs={}
    node_ports = {port['name']: port for port in node.input_desc}
    for p in parameters:
        port = node_ports[p]
        inputs[p] = dict(type=_type(port['interface']), default=port['value'])
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
    model['execution']['endpoint'] = 'http://127.0.0.1:8000/dss/model/{dss_name}/{model_id}/'.format(dss_name=template.dss, model_id=model_id)

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
        config.update(wrap_inputs(node, parameters))
    properties['configParameters']['properties'] = config
    properties['configParameters']['required'] = list(config.keys())
    model['execution']['input_schema']['required'] = ['modelId', 'configParameters']
    model['output'] = wrap_outputs(node, decision_support=decision_support)

    input_mapping = "{'weather_parameters': %s, 'config_params': %s}"%(json.dumps(weather_parameters),json.dumps(parameters))
    dss_service = fastAPI_template.format(dss_name=template.dss, model_id=model_id, input_mapping=input_mapping)
    return model, dss_service