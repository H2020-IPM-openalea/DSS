
import pandas
from openalea.dss import Manager, Model
import openalea.dss.fakers as fakers


h= Manager()

def test_display():
    catalog = h.display()
    assert type(catalog) is pandas.DataFrame 
    assert len(catalog) > 32
    assert all(k in catalog.columns for k in ['dss', 'models', 'pests', 'crops', 'description'])

def test_get_model():
    psi=h.get_model("no.nibio.vips","PSILARTEMP")
    assert isinstance(psi, Model)

def test_create_package():
    wralea, module_name, module = h.create_package('no.nibio.vips')

    assert isinstance(wralea, dict)
    assert module_name == 'no_nibio_vips.py'
    assert module.startswith('from openalea.DSS')

def test_run_model():
    model = h.get_model("no.nibio.vips","PSILARTEMP")
    output = h.run_model(model)
    assert isinstance(output, dict)

def test_run_node():
    dss = h.dss('no.nibio.vips')
    model = dss.get('PSILARTEMP')
    inputs = fakers.node_inputs(model)
    output = model(**inputs)
    assert isinstance(output, dict)
