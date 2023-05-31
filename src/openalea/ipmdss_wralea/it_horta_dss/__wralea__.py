
# This file has been generated at Wed May 31 09:12:11 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.it.horta.dss'

__editable__ = True
__version__ = '1.0'
__institutes__ = 'Horta'
__authors__ = 'Horta'
__description__ = 'Horta-srl'
__url__ = 'https://www.horta-srl.it/'


__all__ = ['openalea_ipmdss_wralea_it_horta_dss_it_horta_dss_tomato_it_horta_dss_tomato', 'openalea_ipmdss_wralea_it_horta_dss_it_horta_dss_wheat_it_horta_dss_wheat']



openalea_ipmdss_wralea_it_horta_dss_it_horta_dss_tomato_it_horta_dss_tomato = Factory(name='it_horta_dss_tomato',
                authors='Horta (wralea authors)',
                description=b'Account required, charges apply. \n\nPhytophthora infestans \nTHE DECISION: Guides application of protection strategies \nTHE MODEL: The tomato late blight model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nAlternaria solani\nTHE DECISION: Application of protection strategies \nTHE MODEL: The tomato early blight model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \nSOURCE: Horta 2023\n\nPseudomonas syringae ; Xanthomonas campestris\nTHE DECISION: Application of protection strategies \nTHE MODEL: The tomato bacterial speck model takes into account the main processes of P. syringae, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nXanthomonas campestris\nTHE DECISION: Application of protection strategies \nTHE MODEL: The tomato bacterial speck model takes into account the main processes of X. campestris, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nSOURCE: All models have been adapted/developed by Horta s.l.r\nhttps://www.horta-srl.it/en/\n',
                category='',
                nodemodule='openalea.ipmdss_wralea.it_horta_dss.it_horta_dss_tomato',
                nodeclass='it_horta_dss_tomato',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_it_horta_dss_it_horta_dss_wheat_it_horta_dss_wheat = Factory(name='it_horta_dss_wheat',
                authors='Horta (wralea authors)',
                description=b'Account required, charges apply. \n\nPuccinia striiformis\nTHE DECISION: Guides application of protection strategies \nTHE MODEL: The yellow stripe rust model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nPuccinia triticina\nTHE DECISION: Application of protection strategies \nTHE MODEL: The brown leaf rust model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nFusarium graminearum\nTHE DECISION: Application of protection strategies \nTHE MODEL: The fusarium head blight model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. The model also provide the probability that the amount of mycotoxins exceeds the legal limit. \n\nZymoseptoria tritici\nTHE DECISION: Application of protection strategies \nTHE MODEL: The septoria model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection of peckled leaf spot (Septoria blotch) in the field. \n\nBlumeria graminis f. sp. tritici\nTHE DECISION: Application of protection strategies \nTHE MODEL: The septoria model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection of powdery mildew of wheat in the field. \n\n\nSOURCE: All models have been adapted/developed by Horta s.l.r\nhttps://www.horta-srl.it/en/\n',
                category='',
                nodemodule='openalea.ipmdss_wralea.it_horta_dss.it_horta_dss_wheat',
                nodeclass='it_horta_dss_wheat',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




