from openalea.core import alea
from collections import OrderedDict

import json
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return str(o)


pm = alea.load_package_manager()
factory = pm['dss']
name = 'dss_model'

def package_metainfo(factory):
    """
    Transform package meta-information in Ordered Dict
    
    parameters:
    -----------
        factory: package name
    """
    identifier = NotImplemented
    name = factory.name
    description = factory.metainfo['description'] # optional no ask by ipm
    version = factory.metainfo['version']
    Authors = factory.metainfo['authors']
    url = factory.metainfo['url']
    languages = NotImplemented
    organization = {"name" : factory.metainfo["institutes"], 
                    "country" : NotImplemented, 
                    "address" : NotImplemented, 
                    "postal_code" : NotImplemented, 
                    "city" : NotImplemented, 
                    "email" : NotImplemented, 
                    "url" : NotImplemented}
    license = factory.metainfo['license'] # optional no ask by ipm

    return OrderedDict(identifier = identifier,
                       name = name,
                       description = description,
                       version = version,
                       Authors = Authors,  
                       url = url, 
                       languages = languages,
                       organization = organization,
                       license = license)

def model_metainfo(factory,name):
    """Transform a factory into an OrderedDict"""
    name = factory[name].name
    identifier = NotImplemented 
    version = NotImplemented
    type_of_decision = NotImplemented
    type_of_output = NotImplemented
    description_URL = NotImplemented
    description = factory[name].description
    citation = NotImplemented
    execution = {"type": NotImplemented,
                "endpoints": NotImplemented,
                "form_method": NotImplemented,
                "content_type": NotImplemented,
                "input_schema": NotImplemented} #factory[name].get_writer()}
    inputs = factory[name].inputs
    authors = {"name":factory[name].get_authors(),
            "email": NotImplemented,
            "organization":factory.metainfo["institutes"]}
    pests = NotImplemented
    crops = NotImplemented
    keywords = NotImplemented
    output = {"warning_status_interpretation": NotImplemented,
            "result_parameters": {"id": NotImplemented , 
                                "title": factory[name].outputs[0]['name'],
                                "description": factory[name].outputs[0]['desc']}}
    valid_spatial = {"countries": NotImplemented,
                    "geoJson": NotImplemented}
    
    return OrderedDict(name = name, 
                       identifier = identifier, 
                       version= version,
                       type_of_decision = type_of_decision,
                       type_of_output = type_of_output,
                       description_URL = description_URL,
                       description = description,
                       citation = citation,
                       execution = execution,
                       input = inputs,
                       authors=authors, 
                       pests = pests,
                       crops = crops,
                       keywords = keywords,
                       output = output,
                       valid_spatial = valid_spatial
                       )


dss = package_metainfo(factory)
model = model_metainfo(factory, name)

def json_read(obj):
    '''
    print Ordered dict in json
    
    Parameters:
    -----------
        obj:  OrderedDict issue from DSS and/or DSSModel function

    return:
    -------
        print in json format of OpenAlea package and model for DSS
    ''' 
    print(json.dumps(obj,indent=4,sort_keys=True, cls=MyEncoder))

json_read(obj=(dss,model))

def json_write(obj, filename):
    ''' 
    Create json file
    
    Parameters:
    -----------
        obj: OrderedDict issue from DSS and/or DSSModel function
        filname: (string) name of json file (filename must be finish by extension .json)

    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(obj,f,indent=4,sort_keys=True,cls=MyEncoder))

#json_write(obj=(dss, model),filename='DSS_package.json')




