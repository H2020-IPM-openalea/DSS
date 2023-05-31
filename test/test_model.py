""" Test DSSData workflow on PSILARTEMP Model
"""


from openalea.dss import Manager
from weatherdata.ipm import WeatherDataHub
import xarray as xr

h= Manager()
psi= h.get_model("no.nibio.vips", "PSILARTEMP")



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
    ws = WeatherDataHub()
    fmi = ws.get_ressource(name='fi.fmi.observation.station')

    weather = fmi.data(stationId=[101533], parameters=[1002], interval=3600, display="json")
    # run Model
    ds= psi.run(weatherdata=weather)
    assert type(ds) is xr.Dataset
    assert list(ds.data_vars)==['TMDD5C', 'THRESHOLD_1', 'THRESHOLD_2', 'THRESHOLD_3']
    assert list(ds.dims)==["time"]
    assert keys_exists(ds.attrs,keys=['name', 'id', 'version', 'authors', 'description', 'description_url'])


