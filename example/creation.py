from openalea.core.node import FuncNode
from openalea.core import IFloat, IInt
from openalea.dss.dss_factory import dss_factory, encode_input, encode_output
import agroservices.ipm.fakers as ipm_fakers

def t_risk(tair, threshold=15):
    if tair <= threshold:
        return 0
    else:
        return 1

decision_support = list(range(2))
decision_support[0] = {'explanation': 'Risk is low',
                      'recommended_action': 'No particular action is required'}
decision_support[1] = {'explanation': 'Risk is high',
                      'recommended_action': 'Be carreful !'}
					  

inputs = (dict(name='tair', interface=IFloat, value=None),
          dict(name='threshold', interface=IFloat, value=15))
outputs = (dict(name='Risk', interface=IInt), )
node = FuncNode(inputs, outputs, t_risk)
node.name='TRISK'
input_mapping = {'weather_parameters': {'tair': 1002}, 'config_params': ['threshold']}


ipm_model, service = dss_factory(node.name, node,decision_support=decision_support, **input_mapping)

input_data = ipm_fakers.input_data(ipm_model)
inputs = encode_input(node, input_data, input_mapping)
output_data = [node(input) for input in inputs]
if len(node.output_desc) == 1:
    output_data = [list((item,)) for item in output_data]
resp = encode_output(node, input_data, output_data)