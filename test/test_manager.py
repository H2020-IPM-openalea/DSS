
import pandas
from openalea.dss import Manager, Model

h= Manager()

catalog= h.display()

def test_catalog_display():
    assert type(catalog) is pandas.DataFrame 
    assert len(catalog) > 32
    assert all(k in catalog.columns for k in ['dss', 'models', 'pests', 'crops', 'description'])

def test_get_model():
    psi=h.get_model("no.nibio.vips","PSILARTEMP")
    assert isinstance(psi, Model)  

