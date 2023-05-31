
# This file has been generated at Wed May 31 02:30:32 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.dk.au.agro'

__editable__ = True
__version__ = '1.0'
__institutes__ = 'Aarhus University, Department of Agroecology'
__authors__ = 'Aarhus University, Department of Agroecology'
__description__ = 'Aarhus University RustWatch'
__url__ = 'https://agro.au.dk/forskning/projekter/rustwatch/wheat-rust-early-warning'


__all__ = ['ipmdecisions_dss_dk_au_agro_YellowRustEarlyWarning_YellowRustEarlyWarning', 'ipmdecisions_dss_dk_au_agro_StemRustGeneticFrequency_StemRustGeneticFrequency', 'ipmdecisions_dss_dk_au_agro_LeafRustGeneticGroupFrequency_LeafRustGeneticGroupFrequency', 'ipmdecisions_dss_dk_au_agro_YellowRustGeneticGroupFrequency_YellowRustGeneticGroupFrequency']



ipmdecisions_dss_dk_au_agro_YellowRustEarlyWarning_YellowRustEarlyWarning = Factory(name='YellowRustEarlyWarning',
                authors='Aarhus University, Department of Agroecology (wralea authors)',
                description=b'RustWatch is an established stakeholder driven early-warning system to improve preparedness and resilience to emerging rust diseases on wheat. Rust diseases are very dynamic, which makes  it very important to follow changes in aggressiveness and spreading pattern, e.g. the existing population of wheat yellow rust has been replaced by invasive races of non-European origin (2011) and since 2016 Europe has experienced more severe epidemics of wheat stem rust. If you want more detailed information about the collected rust data, take a look at the GRRC platform.  https://gis-au.maps.arcgis.com/apps/dashboards/6817a33478df49d39176863fdc67fe15\nRustWatch partners keep an eye on the development of rust species and races in order to evaluate  their potential impact on agricultural productivity. and finally develop research and communication  infrastructures including stakeholder networks.. The research and phenotyping is essential for the  plant breeders screening for new resistant cultivars.\nRustWatch engages 12 universities/research institutes, 5 agricultural advisory services, and 7  SMEs/industries. After the project ended in 2022, RustWatch is now a \xe2\x80\x9cRustWatch - a wheat rust  network for Europe\xe2\x80\x9d. Pan-European surveillance, race phenotyping and other research activities will  continue based on coordination of related projects, national activities and agreed business models.  Everybody interested in early warning and wheat rust diseases are welcome to join this network and  participate in RustWatch activities.\n',
                category='Yellow rust',
                nodemodule='ipmdecisions.dss.dk.au.agro.YellowRustEarlyWarning',
                nodeclass='YellowRustEarlyWarning',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_au_agro_StemRustGeneticFrequency_StemRustGeneticFrequency = Factory(name='StemRustGeneticFrequency',
                authors='Aarhus University, Department of Agroecology (wralea authors)',
                description=b'RustWatch is an established stakeholder driven early-warning system to improve preparedness  and resilience to emerging rust diseases on wheat. Rust diseases are very dynamic, which makes  it very important to follow changes in aggressiveness and spreading pattern, e.g. the existing  population of wheat yellow rust has been replaced by invasive races of non-European origin (2011)  and since 2016 Europe has experienced more severe epidemics of wheat stem rust. If you want more  detailed information about the collected rust data, take a look at the GRRC platform.  https://gis-au.maps.arcgis.com/apps/dashboards/6817a33478df49d39176863fdc67fe15\nRustWatch partners keep an eye on the development of rust species and races in order to evaluate  their potential impact on agricultural productivity. and finally develop research and communication  infrastructures including stakeholder networks.. The research and phenotyping is essential for the  plant breeders screening for new resistant cultivars.\nRustWatch engages 12 universities/research institutes, 5 agricultural advisory services, and 7  SMEs/industries. After the project ended in 2022, RustWatch is now a \xe2\x80\x9cRustWatch - a wheat rust  network for Europe\xe2\x80\x9d. Pan-European surveillance, race phenotyping and other research activities will  continue based on coordination of related projects, national activities and agreed business models.  Everybody interested in early warning and wheat rust diseases are welcome to join this network and  participate in RustWatch activities.\n',
                category='',
                nodemodule='ipmdecisions.dss.dk.au.agro.StemRustGeneticFrequency',
                nodeclass='StemRustGeneticFrequency',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_au_agro_LeafRustGeneticGroupFrequency_LeafRustGeneticGroupFrequency = Factory(name='LeafRustGeneticGroupFrequency',
                authors='Aarhus University, Department of Agroecology (wralea authors)',
                description=b'RustWatch is an established stakeholder driven early-warning system to improve preparedness  and resilience to emerging rust diseases on wheat. Rust diseases are very dynamic, which makes  it very important to follow changes in aggressiveness and spreading pattern, e.g. the existing  population of wheat yellow rust has been replaced by invasive races of non-European origin (2011)  and since 2016 Europe has experienced more severe epidemics of wheat stem rust. If you want more  detailed information about the collected rust data, take a look at the GRRC platform.  https://gis-au.maps.arcgis.com/apps/dashboards/6817a33478df49d39176863fdc67fe15\nRustWatch partners keep an eye on the development of rust species and races in order to evaluate  their potential impact on agricultural productivity. and finally develop research and communication  infrastructures including stakeholder networks.. The research and phenotyping is essential for the  plant breeders screening for new resistant cultivars.\nRustWatch engages 12 universities/research institutes, 5 agricultural advisory services, and 7  SMEs/industries. After the project ended in 2022, RustWatch is now a \xe2\x80\x9cRustWatch - a wheat rust  network for Europe\xe2\x80\x9d. Pan-European surveillance, race phenotyping and other research activities will  continue based on coordination of related projects, national activities and agreed business models.  Everybody interested in early warning and wheat rust diseases are welcome to join this network and  participate in RustWatch activities.',
                category='',
                nodemodule='ipmdecisions.dss.dk.au.agro.LeafRustGeneticGroupFrequency',
                nodeclass='LeafRustGeneticGroupFrequency',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_au_agro_YellowRustGeneticGroupFrequency_YellowRustGeneticGroupFrequency = Factory(name='YellowRustGeneticGroupFrequency',
                authors='Aarhus University, Department of Agroecology (wralea authors)',
                description=b'RustWatch is an established stakeholder driven early-warning system to improve preparedness  and resilience to emerging rust diseases on wheat. Rust diseases are very dynamic, which makes  it very important to follow changes in aggressiveness and spreading pattern, e.g. the existing  population of wheat yellow rust has been replaced by invasive races of non-European origin (2011)  and since 2016 Europe has experienced more severe epidemics of wheat stem rust. If you want more  detailed information about the collected rust data, take a look at the GRRC platform.  https://gis-au.maps.arcgis.com/apps/dashboards/6817a33478df49d39176863fdc67fe15\nRustWatch partners keep an eye on the development of rust species and races in order to evaluate  their potential impact on agricultural productivity. and finally develop research and communication  infrastructures including stakeholder networks.. The research and phenotyping is essential for the  plant breeders screening for new resistant cultivars.\nRustWatch engages 12 universities/research institutes, 5 agricultural advisory services, and 7  SMEs/industries. After the project ended in 2022, RustWatch is now a \xe2\x80\x9cRustWatch - a wheat rust  network for Europe\xe2\x80\x9d. Pan-European surveillance, race phenotyping and other research activities will  continue based on coordination of related projects, national activities and agreed business models.  Everybody interested in early warning and wheat rust diseases are welcome to join this network and  participate in RustWatch activities.',
                category='',
                nodemodule='ipmdecisions.dss.dk.au.agro.YellowRustGeneticGroupFrequency',
                nodeclass='YellowRustGeneticGroupFrequency',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




