
# This file has been generated at Wed May 31 10:34:52 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.Best4Soil.Support.Tools'

__editable__ = True
__version__ = '1.0'
__institutes__ = 'Wageningen University and Research'
__authors__ = 'Wageningen University and Research'
__description__ = 'Best4Soil DSS for nematodes and soil borne diseases'
__url__ = 'https://www.best4soil.eu/database'


__all__ = ['openalea_ipmdss_wralea_Best4Soil_Support_Tools_nematodes_nematodes', 'openalea_ipmdss_wralea_Best4Soil_Support_Tools_pathogens_pathogens']



openalea_ipmdss_wralea_Best4Soil_Support_Tools_nematodes_nematodes = Factory(name='nematodes',
                authors='Wageningen University and Research (wralea authors)',
                description=b'THE PEST: Plant parasitic nematodes can cause serious damage to crop yield and crop quality. Important groups of plant parasitic nematodes are: cyst nematodes, root-knot nematodes, root-lesions nematodes, stem nematodes and free living nematodes. THE DECISION: Nematodes can best be managed by healthy crop rotations, as crops and crop varieties have a different host status for nematodes. Alternating host and non-host crops or varieties lowers infestation rates in the soil. THE MODEL: The model databases contain information about susceptibility and tolerance of 70 crops to 32 nematodes. The databases are neither soil-specific nor country-specific. PARAMETERS: The returns risks based on crops, including green manure crops, and crop rotation. This farm specific input has to be provided by the user. SOURCE: Created by H2020 project Best4Soil, based on the Dutch model www.aaltjesschema.nl, developed by Wageningen University and Research. ASSUMPTIONS: The model gives risk information, assuming that the user selected plant parasitic nematodes are present in the field.',
                category=None,
                nodemodule='openalea.ipmdss_wralea.Best4Soil_Support_Tools.nematodes',
                nodeclass='nematodes',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_Best4Soil_Support_Tools_pathogens_pathogens = Factory(name='pathogens',
                authors='Wageningen University and Research (wralea authors)',
                description=b'THE PEST: Soil-borne pathogens can cause serious damage to crop yield and quality. Major groups of such pathogens are: Fusarium, Phoma, Phomopsis, Phytophthora, Pythium, Rhizoctonia and Sclerotinia. Soil-borne pathogens can often be managed by crop rotations, as they infect only certain crop species and usually decline in the absence of a host crop.  A rotation containing non-host crops or varieties can lower infestation rates in the soil. THE MODEL: The model databases contain information about susceptibility and tolerance of 70 crops to 135 pathogens. PARAMETERS: The model uses crops, including green manure crops, and crop rotation. This farm specific input has to be provided by the user. SOURCE: Created by H2020 project Best4Soil, analogue to the Dutch model www.aaltjesschema.nl, developed by Wageningen University and Research. ASSUMPTIONS: The model gives risk information, assuming that the user selected plant pathogens are present in the field. At the moment, the databases are neither soil-specific, nor country-specific. This means that the crop schemes are identical for different soil types and countries. At this moment there is insufficient country-specific information on host status and sensitivity to crop damage per crop to make the database country-specific. The same is the case for soil type specific information. Because soil type plays a role in the occurrence of  soil pathogens, the soil type selection button has been built in to enable soil type specific schemes in the future. ',
                category='Soil borne pathogens ',
                nodemodule='openalea.ipmdss_wralea.Best4Soil_Support_Tools.pathogens',
                nodeclass='pathogens',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




