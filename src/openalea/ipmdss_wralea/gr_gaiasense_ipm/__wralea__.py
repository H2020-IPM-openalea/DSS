
# This file has been generated at Wed May 31 10:34:52 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.gr.gaiasense.ipm'

__editable__ = True
__version__ = '0.1'
__institutes__ = 'NEUROPUBLIC'
__authors__ = 'NEUROPUBLIC'
__description__ = 'gaiasense'
__url__ = 'https://www.gaiasense.gr'


__all__ = ['openalea_ipmdss_wralea_gr_gaiasense_ipm_PLASVI_PLASVI']



openalea_ipmdss_wralea_gr_gaiasense_ipm_PLASVI_PLASVI = Factory(name='PLASVI',
                authors='NEUROPUBLIC (wralea authors)',
                description=b'The warning system model \xc2\xabDowny mildew of grapevine\xc2\xbb is based on prediction model that utilises as input the following parameters: temperatute, humidity and leaf-wetness. Also the current growth stage of the plant is considered.(this description to be further updated)\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='none',
                nodemodule='openalea.ipmdss_wralea.gr_gaiasense_ipm.PLASVI',
                nodeclass='PLASVI',
                inputs=[{'name': 'WeatherSource', 'value': None}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




