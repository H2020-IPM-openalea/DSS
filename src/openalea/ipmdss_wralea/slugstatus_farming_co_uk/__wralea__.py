
# This file has been generated at Wed May 31 10:34:52 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.slugstatus.farming.co.uk'

__editable__ = True
__version__ = '1.0'
__institutes__ = 'Farming Online Ltd'
__authors__ = 'Farming Online Ltd'
__description__ = 'SlugWatch'
__url__ = 'http://slugstatus.farming.co.uk/postcode/'


__all__ = ['openalea_ipmdss_wralea_slugstatus_farming_co_uk_SlugWatch2023_SlugWatch2023']



openalea_ipmdss_wralea_slugstatus_farming_co_uk_SlugWatch2023_SlugWatch2023 = Factory(name='SlugWatch2023',
                authors='Farming Online Ltd (wralea authors)',
                description=b'THE PEST: Widely present in many horticultural and arable fields, slugs can damage crops all year round. With impacts on yield and/or quality potentially severe, it is important to manage populations of key slug species. \nTHE DECISION: Management of slug infestations is most effective when targeted at periods of high slug activity. The SlugWatch forecast provides location-specific slug activity data, along with information on weather conditions, helping make informed decisions on timing and location of slug monitoring and subsequent management. \nTHE MODEL: The SlugWatch model predicts slug activity based on forecast weather conditions. \nTHE PARAMETERS: The model uses soil temperature, air temperature and rainfall. \nSOURCE: Created by CertisBelchim and developed by Farming Online Ltd. Validated in the UK and France, considered to be appropriate for use with caution in Ireland, Spain, Belgium the Netherlands, Germany, and Denmark. \nASSUMPTIONS: This model makes no prediction on actual slug abundance, only the relative risk of slug activity if they are present. In field monitoring is required to assess the actual risk to crops of high slug activity. Please refer to appropriate economic thresholds for treatment. ',
                category='',
                nodemodule='openalea.ipmdss_wralea.slugstatus_farming_co_uk.SlugWatch2023',
                nodeclass='SlugWatch2023',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




