"""A module that allow exporting an openalea node/factory as an IPM model"""

fastAPI_template="""from fastapi import FastAPI

app = FastAPI()

@app.post("dss/model/%s/%s")
async def model_evaluation(item):
    return item
"""

def wrap_inputs(node):
    return node

def wrap_outputs(node):
    return node

def dss_factory(node, interval=86400, weather_parameters=None, parameters=None, template=None):
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
    model['execution']['endpoint'] = 'http://127.0.0.1:8000'
    if weather_parameters is None:
        model['input']['weather_parameters'] = None
    else:
        model['input']['weather_parameters'] = [{'parameter_code': v, 'interval': interval} for v in weather_parameters.values()]

    properties = model['execution']['input_schema']['properties']
    properties['modelId']['pattern'] = '^%s$'%(model_id)
    properties['modelId']['default'] = model_id
    properties['modelId']['description'] = 'Must be %s'%(model_id)
    #properties.pop('timeZone')
    #model['execution']['input_schema']['required'] = ['modelId', 'configParameters']

    dss_service = fastAPI_template%(template.dss, model_id)
    return model, dss_service