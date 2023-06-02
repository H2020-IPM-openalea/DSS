from openalea.core.node import FuncNode
from openalea.core import IFloat, IInt
from openalea.dss import Manager
from openalea.dss.dss_factory import dss_factory


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
					  
m = Manager()
template = m.get_model("no.nibio.vips","PSILARTEMP")

inputs = (dict(name='tair', interface=IFloat, value=None),
          dict(name='threshold', interface=IFloat, value=15))
outputs = (dict(name='Risk', interface=IInt), )
my_node = FuncNode(inputs, outputs, t_risk)
my_node.name='TRISK'

ipm_model, service = dss_factory(my_node, weather_parameters={'tair': 1002}, parameters=['threshold'],decision_support=decision_support,template=template)