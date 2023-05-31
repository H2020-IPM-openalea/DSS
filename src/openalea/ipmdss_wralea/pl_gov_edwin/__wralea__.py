
# This file has been generated at Wed May 31 10:34:52 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.pl.gov.edwin'

__editable__ = True
__version__ = '0.0.2'
__institutes__ = 'Institute of Bioorganic Chemistry of the Polish Academy of Sciences -  Poznan Supercomputing and Networking Center'
__authors__ = 'Institute of Bioorganic Chemistry of the Polish Academy of Sciences -  Poznan Supercomputing and Networking Center'
__description__ = 'eDWIN'
__url__ = 'https://www.edwin.gov.pl/'


__all__ = ['openalea_ipmdss_wralea_pl_gov_edwin_eDWIN_LINK_eDWIN_LINK']



openalea_ipmdss_wralea_pl_gov_edwin_eDWIN_LINK_eDWIN_LINK = Factory(name='eDWIN_LINK',
                authors='Institute of Bioorganic Chemistry of the Polish Academy of Sciences -  Poznan Supercomputing and Networking Center (wralea authors)',
                description=b'The eDWIN "Virtual farm" allows users in Poland to obtain, collect and share information about the occurrence of pests in a given area and provides notifications about possible threats in the field.\nThe eDWIN platform, also provides access to data from about 600 meteorological stations throughout Poland, monitoring (among others) temperature, air humidity, rainfall total and intensity, atmospheric pressure and wind speed and direction.\nThe eDWIN advisory platform was created as part of the project "Internet Platform for Advisory and Decision Support in Integrated Plant Protection". \nThe platform is completely free and available to everyone on computers and as an application on mobile devices, but only currently accessible to users in Poland. \n\nhttps://www.edwin.gov.pl/euslugi/wirtualne-gospodarstwo',
                category='',
                nodemodule='openalea.ipmdss_wralea.pl_gov_edwin.eDWIN_LINK',
                nodeclass='eDWIN_LINK',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




