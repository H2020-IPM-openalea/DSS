from openalea.core import alea
from collections import OrderedDict

import json
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return str(o)


def json_convert(package_name, module_name):
    ''' convert openalea metainfo package and module in json
    
    parameters:
    -----------
       package_name: name of package to convert (type:string)
       module_name : name of python module of package (type:string)
    
    Return:
    -------
       print of metainformation in json according to IPM schema

    '''
    pm = alea.load_package_manager()
    
    factory = pm[package_name]
    name = module_name

    def DSS(factory):
        """Transform package meta-information in Ordered Dict"""
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

    def DSSModel(factory,name):
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
                    "input_schema": factory[name].get_writer()}
        inputs = factory[name].inputs
        authors = [{"name":factory[name].get_authors(),
                "email": NotImplemented,
                "organization":factory.metainfo["institutes"]}
                ]
        pests = NotImplemented
        crops = NotImplemented
        keywords = NotImplemented
        output = {"warning_status_interpretation": NotImplemented,
                "result_parameters": [{"id": NotImplemented , 
                                    "title": factory[name].outputs[0]['name'],
                                    "description": factory[name].outputs[0]['desc']}]}
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
    
    print json.dumps({"DSS":DSS(factory), "models":[DSSModel(factory,name)]}, indent=4, sort_keys=True, cls=MyEncoder)