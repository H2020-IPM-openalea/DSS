
import pandas
from openalea.dss import Hub, Model

h= Hub()

catalog= h.display()

def test_catalog_display():
    assert type(catalog) is pandas.DataFrame 
    assert len(catalog) > 32
    assert all(k in catalog.columns for k in ['dss', 'models', 'pests', 'crops', 'description'])

def test_get():
    psi=h.get(dss="no.nibio.vips",model="PSILARTEMP")
    assert isinstance(psi, Model)  

