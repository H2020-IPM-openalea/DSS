
# This file has been generated at Wed May 31 02:30:32 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.nl.wur.IWMPRAISE'

__editable__ = True
__version__ = '1.0'
__institutes__ = 'Wageningen University and Research'
__authors__ = 'Wageningen University and Research'
__description__ = 'IWMPRAISE Integrated Weed Management Tool'
__url__ = 'https://framework.iwmtool.eu/ '


__all__ = ['ipmdecisions_dss_nl_wur_IWMPRAISE_IWMPRAISE_Tool_IWMPRAISE_Tool']



ipmdecisions_dss_nl_wur_IWMPRAISE_IWMPRAISE_Tool_IWMPRAISE_Tool = Factory(name='IWMPRAISE_Tool',
                authors='Wageningen University and Research (wralea authors)',
                description=b'THE PEST: Perennial and annual weed infestations can lead to direct and indirect damage to a wide range of outdoor crops. \nTHE DECISION: Integrated weed management tactics may affect one or more axes in the weed life cycle. They may prevent the establishment of seedlings from the seedbank (axis 1), reduce the impact established weeds have on the crop (axis 2), or reduce the weed seed/bud return to the soil (axis 3).\nTHE IWMPRAISE TOOL: This tool supports users in identifying and understanding the IPM tools and tactics available to manage perennial and annual weeds in narrow row, broad row and perennial crops. Users can select/de-select options to identify the best approach for them. This tool is currently available in English only. \nSOURCE: The IWMPRAISE TOOL was developed as part of the EU funded Horizon 2020 IWMPRAISE (727321), 2017-2022. It is designed for use across Europe.  \nREFERENCE: Kudsk et al (2020) Outlooks on Pest Management, 31, 152-159, https://doi.org/10.1564/v31_aug_02\n ',
                category='Annual, perennial, weeds ',
                nodemodule='ipmdecisions.dss.nl.wur.IWMPRAISE.IWMPRAISE_Tool',
                nodeclass='IWMPRAISE_Tool',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




