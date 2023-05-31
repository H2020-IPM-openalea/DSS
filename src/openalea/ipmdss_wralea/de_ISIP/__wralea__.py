
# This file has been generated at Wed May 31 09:12:11 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.de.ISIP'

__editable__ = True
__version__ = '1.0'
__institutes__ = 'ISIP (technical contact), ZEPP (agronomic contact)'
__authors__ = 'ISIP (technical contact), ZEPP (agronomic contact)'
__description__ = 'ISIP'
__url__ = 'www.isip.de'


__all__ = ['openalea_ipmdss_wralea_de_ISIP_siggetreide_siggetreide']



openalea_ipmdss_wralea_de_ISIP_siggetreide_siggetreide = Factory(name='siggetreide',
                authors='ISIP (technical contact), ZEPP (agronomic contact) (wralea authors)',
                description=b'With weather-based forecast models for pests and diseases, you can calculate the occurrence of pathogens and periods  of high infestation pressure. Infestation controls and recommendations from the plant protection services also inform you about the  current situation in your region. In addition, programs are available for calculating plant development and choosing the most  suitable tillage system.',
                category=None,
                nodemodule='openalea.ipmdss_wralea.de_ISIP.siggetreide',
                nodeclass='siggetreide',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




