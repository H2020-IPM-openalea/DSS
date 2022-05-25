""" Test DSSData workflow on PSILARTEMP Model
"""


from setuptools import sic
from openalea.dss import Hub
from weatherdata.ipm import WeatherDataHub
import xarray as xr

h= Hub()
psi= h.get(dss="no.nibio.vips",model="PSILARTEMP")



def keys_exists(dict_, keys, test = all):
    return test(key in dict_ for key in keys)

def test_information():
    
    rep_json=psi.informations()
    assert type(rep_json) is dict
    assert keys_exists(rep_json,keys=['name', 'id', 'version', 'purpose', 'description', 'type_of_decision', 'type_of_output', 'description_URL', 
                                      'citation', 'keywords', 'platform_validated', 'pests', 'crops', 'authors', 'execution', 'input', 'valid_spatial', 'output'])
    
    rep= psi.informations("dataframe")
    assert rep.shape == (1,10)
    assert any(rep.columns==['name', 'id', 'description', 'type_of_decision', 'pests', 'crops',
       'weather input', 'field_observation input', 'output',
       'output_description'])
    
def test_run():
    # Weatherdata
    ws=WeatherDataHub()
    slu=ws.get_ressource(name="SLU Lantmet service")

    weather=slu.data(parameters=[1002],latitude=[67.28],longitude=[14.37],
                    timeStart='2021-06-01',timeEnd="2021-08-20",timeZone="Europe/Paris",
                    display="json")
    
    # run Model
    ds= psi.run(weatherdata=weather)
    assert type(ds) is xr.Dataset
    assert list(ds.data_vars)==['TMDD5C', 'THRESHOLD_1', 'THRESHOLD_2', 'THRESHOLD_3']
    assert list(ds.dims)==["time"]
    assert ds.sizes==81
    assert keys_exists(ds.attrs,keys=['name', 'id', 'version', 'authors', 'description', 'description_url'])

    return ds

