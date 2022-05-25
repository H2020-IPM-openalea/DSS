
import pandas
from openalea.dss import Hub, Model

h= Hub()

catalog= h.display()

def test_catalog_display():
    catalog
    assert type(catalog) is pandas.DataFrame 
    assert catalog.shape == (32,5)
    assert any(catalog.columns == ['dss', 'models', 'pests', 'crops', 'description'])

def test_get():
    psi=h.get(dss="no.nibio.vips",model="PSILARTEMP")
    assert isinstance(psi, Model)  

