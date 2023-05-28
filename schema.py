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
        """Transform an openalea package into a DSS meta-information Ordered Dict
        On IPM, a DSS is a collection of models
        The mapping between nodes of the package and DSS models is described in DSSModel
        
        elaborated from "https://ipmdecisions.nibio.no/api/dss/rest/schema/dss"
        """
        # required
        #models  = To be collected/aggregated from DSSmodel
        id = NotImplemented # A unique id for the DSS, example"no.nibio.vips"
        version = factory.metainfo['version']
        name = factory.name
        url = factory.metainfo['url']
        languages = ["English"] #"A list of languages that the DSS supports"
        organization = {
                "name" : factory.metainfo["institutes"], 
                "country" : NotImplemented, 
                "address" : NotImplemented, 
                "postal_code" : NotImplemented, 
                "city" : NotImplemented, 
                "email" : factory.metainfo['authors'][0], 
                "url" : NotImplemented}
        # additional properties
        additionalProperties = {
            "description" : factory.metainfo['description']
            "license": factory.metainfo['license']
            }
    
        return OrderedDict(models = {},
                           id = id,
                           version = version, 
                           name = name,
                           url = url, 
                           languages = languages,
                           organization = organization,
                           additionalProperties = additionalProperties)

    def DSSModel(factory,name):
        """Transform a factory into an OrderedDict representing a model belonging to a DSS
        
        elaborated from "https://ipmdecisions.nibio.no/api/dss/rest/schema/dss"
        """
        # required
        id = factory[name].name # "(string) A unique ID for the model in the namespace of the DSS. Exemple PSILARTEMP"
        name = NotImplemented #could be first line of docstring ? Exemple : "Carrot rust fly temperature model"
        version = factory.metainfo['version']
        # additionnal
        type_of_decision = "" #	"Describing what kind of decision the model gives advice on", eg "Short-term tactical"
        type_of_output = "" # "What kind of output does the model give", eg "Risk indication"
        description_URL = "" # "A URL to more description about the model", readthedoc address ?
        description = factory[name].description,
        citation = "" #"Any literature references for the model"
        keywords = "" #"keywords to make this model searchable"
        platform_validated = False #"If not true, the model is not ready to be used on the platform"
        pests = [] # (listofstrings) "A list of EPPO codes for the pests predicted by this model"
        crops = [] # (listofstrings) "A list of EPPO codes for the crops in which this model predicts pests"
        authors = [{"name":factory[name].get_authors(),
        "email": NotImplemented,
        "organization":factory.metainfo["institutes"]}
        ]
        execution = {"type": "ONTHEFLY",
                    "endpoint": "", # adress of web service
                    "form_method": 'post',
                    "content_type":"application/json",
                    "input_schema": NotImplemented}# to be derived from factory[name].get_writer(), with capture/usage of input type : config parameter, weather data, field observation
        inputs = NotImplemented, # to be derived from factory[name].inputs, with capture/usage of input type : config parameter, weather data, field observation
        valid_spatial = {"countries": "", #"Where is this model confirmed to work? Describe either by a list of countries or by (a) polygon(s) in GeoJson format"
                        "geoJson": {}}
        output = {
                # required
                "warning_status_interpretation": [{'explanation':'', 'recomended_action': ''}] * 5 # a 5 items list of warning status description, eg explanation :"The flight period of the 1st generation is over", recomended_action :"Consult your advisory service"  
                "result_parameters": [{"id": item['name'] , 
                                    "title": item['name'],
                                    "description": item['desc']
                                    # additional
                                    #"chart_info": {'default_visible': False, 'unit': "", 'chart_type': '', 'color':''}
                                    }  for item in factory[name].outputs]
                                    ],
                "chart_groups": [] # a list of chart specs: {'id': "", 'title': "", 'result_parameters_ids':[""]},
                # additional
                "chart_heading":""}

        
        return OrderedDict(name = name, 
                        id = id, 
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