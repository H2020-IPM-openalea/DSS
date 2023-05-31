
# This file has been generated at Wed May 31 02:30:32 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.dk.seges'

__editable__ = True
__version__ = '1.1'
__institutes__ = 'SEGES'
__authors__ = 'SEGES'
__description__ = 'SEGES DSS models'
__url__ = 'https://www.seges.dk/'


__all__ = ['ipmdecisions_dss_dk_seges_SEPTORIAHU_SEPTORIAHU', 'ipmdecisions_dss_dk_seges_CPO_HORVX_ERYSGR_CPO_HORVX_ERYSGR', 'ipmdecisions_dss_dk_seges_CPO_HORVX_PUCCHD_CPO_HORVX_PUCCHD', 'ipmdecisions_dss_dk_seges_CPO_HORVX_PYRNTE_CPO_HORVX_PYRNTE', 'ipmdecisions_dss_dk_seges_CPO_TRZAX_ERYSGR_CPO_TRZAX_ERYSGR', 'ipmdecisions_dss_dk_seges_CPO_TRZAX_PUCCST_CPO_TRZAX_PUCCST', 'ipmdecisions_dss_dk_seges_CPO_TRZAX_SEPTTR_CPO_TRZAX_SEPTTR', 'ipmdecisions_dss_dk_seges_CPO_TRZAX_PUCCRE_CPO_TRZAX_PUCCRE', 'ipmdecisions_dss_dk_seges_CPO_TRZAX_PYRNTR_CPO_TRZAX_PYRNTR']



ipmdecisions_dss_dk_seges_SEPTORIAHU_SEPTORIAHU = Factory(name='SEPTORIAHU',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: Leaf blotch diseases of wheat can be caused by septoria tritici blotch (Zymoseptoria tritici) and staganospora nodorum blotch (Parastagonospora nodorum), which are both  favoured by wet conditions. \nTHE DECISION: Fungicide treatments may need to be applied between stem extension and ear emergence, mainly to protect the upper leaves.  \nTHE MODEL: Weather data from GS 31 are used. The humidity model estimates risk of septoria tritici blotch infections in winter wheat. Risk of attack is assumed after 20 hours with continuous wetness. A wet hour is defined as minimum 0,2 mm precipitation in an hour or minimum 85% relative humidity. \nTHE PARAMETERS:  Dates of key growth stages are given as default values, but these may not be correct for your location.  To obtain accurate risk predictions it is essential to click on the 'Edit parameters' button, enter the estimated dates of GS31 (first node detectable), GS32 (second node; third upper leaf emerging), GS33 (third node; second upper leaf emerging), GS37/39 (uppermost flag leaf emerging)  and GS75 (grain content milky), then click on the 'Save' button.  These estimated dates can be updated during the season as growth stages are reached. Adding information on septoria fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the spray dates entered.  After spraying, the model assumes that the crop is protected for 10 days.   \nSOURCE: Created by Aahus University and SEGES and released in Denmark in 2017. Tested in Lithuania, Norway, Sweden, Finland and Denmark in 2018 and 2019. \nASSUMPTIONS: septoria tritici blotch is present in the crop and periods with high humidity create risk for a damaging epidemic\n",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.SEPTORIAHU',
                nodeclass='SEPTORIAHU',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'p2', 'interface': IInt, 'value': 3002}, {'name': 'p3', 'interface': IInt, 'value': 3101}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_HORVX_ERYSGR_CPO_HORVX_ERYSGR = Factory(name='CPO_HORVX_ERYSGR',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: powdery mildew (Blumeria graminis) can attack barley. \nTHE DECISION: Fungicide treatments may need to be applied between early tillering (GS 26)  and full flowering (GS 65), to protect leaves from powdery mildew and yield losses. \nTHE MODEL: The CPO powdery mildew model is recommending treatments in barley when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked.  The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%. In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended, specific fungicides known to be effective against this disease should be chosen.  When running the powdery mildew model, the risk for yield losses from other diseases is not considered. If no action is recommended it is advised to revisit the crop after about one week to make a new evaluation of the risk. \n  \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button to enter information on the cultivar's susceptibility to powdery mildew. Only two categorizes are used susceptible and resistant, if a cultivar is categorized as partly resistant,  it is recommended to considered it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by powdery mildew based on scouting the crop. Between GS  29-31 whole crop should be assessed. Between GS 32 and 40 assessments should only be done on 3 upper leaves.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the information entered and the model will immediately update the risk estimate.  After spraying, the model assumes that the crop is protected for  14 days if a broad spectrum fungicide has been applied.\n     \nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific mildew part.  This model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_HORVX_ERYSGR',
                nodeclass='CPO_HORVX_ERYSGR',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_HORVX_PUCCHD_CPO_HORVX_PUCCHD = Factory(name='CPO_HORVX_PUCCHD',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: Brown rust (Puccinia hordei ) is known to attack barley. \nTHE DECISION: Fungicide treatments may need to be applied between start of elongation  (GS 30)  and full flowering (GS 65), to protect leaves from attack of brown rust and yield losses. \nTHE MODEL: The CPO brown rust model is recommending treatments in barley when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked.   In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended, specific fungicides known to be effective against barley brown rust  should be chosen.  When running the brown rust model the risk for yield losses from other diseases is not considered.   If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to brown rust. Only two categorizes are used susceptible and resistant, if a cultivar is categorized as partly resistant,  it is recommended to consider it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by brown rust based on scouting the crop.  The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%. Between GS  30-31 whole crop should be assessed. Between GS 32 and 65 assessments should be based only on 3 upper leaves.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.   Clicking on 'Save' will keep the observations entered and the model will immediately update the risk.  After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific brown rust part.  This model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_HORVX_PUCCHD',
                nodeclass='CPO_HORVX_PUCCHD',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_HORVX_PYRNTE_CPO_HORVX_PYRNTE = Factory(name='CPO_HORVX_PYRNTE',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: net blotch (Pyrenophora teres) is known to attack barley. \nTHE DECISION: Fungicide treatments may need to be applied between start of elongation  (GS 30)  and full flowering (GS 65), to protect leaves from attack of net blotch and yield losses. \nTHE MODEL: The CPO net blotch model is recommending treatments in barley when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked.  The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%. In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended specific fungicides known to be effective against net blotch  should be chosen.  When running the net blotch model, the risk for yield losses from other diseases is not considered.   If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to net blotch. Only two categorizes are used susceptible and resistant, if a cultivar is categorized as partly resistant, it is recommended to consider it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by net blotch based on scouting the crop. Between GS  30-31 whole plants should be assessed. Between GS 32 and 65 assessments should be based only on 3 upper leaves.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the observations entered and the model will update the risk.  After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific barley net blotch part.  This model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_HORVX_PYRNTE',
                nodeclass='CPO_HORVX_PYRNTE',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_TRZAX_ERYSGR_CPO_TRZAX_ERYSGR = Factory(name='CPO_TRZAX_ERYSGR',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: powdery mildew (Blumeria graminis) is known to attack wheat  \nTHE DECISION: Fungicide treatments may need to be applied between late tillering (GS 29)  and before heading (GS 40), to protect leaves from attack of powdery mildew and yield losses. \nTHE MODEL: The CPO powdery mildew model is recommending treatments in wheat when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked.  The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%. In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended specific fungicides known to be effective against this disease should be chosen.  When running the powdery mildew model the risk for yield losses from other diseases is not considered.   If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to powdery mildew.  Only two categories are used susceptible and resistant, if a cultivar is categorised as partly resistant, we recommend that it is considered as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by powdery mildew based on scouting the crop.  Between GS  29-31 infection on whole plants should be assessed. Between GS 32 and 40 assessments should only be done on 3 upper leaves.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.   Clicking on 'Save' will keep the observations entered and update the risk.  After spraying, the model assumes that the crop is protected for  14 days if a broad spectrum fungicide has been applied.\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific powdery mildew part.   The model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_TRZAX_ERYSGR',
                nodeclass='CPO_TRZAX_ERYSGR',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_TRZAX_PUCCST_CPO_TRZAX_PUCCST = Factory(name='CPO_TRZAX_PUCCST',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: Yellow rust  (Puccinia striiformis) is known to attack wheat  THE DECISION: Fungicide treatments may need to be applied between end of tillering (GS 29) and beginning of grain filling (GS 71) to protect leaves from attack of yellow rust and yield losses.  THE MODEL: The CPO yellow rust model is recommending treatments in wheat when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked. The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 80 plants are completely healthy, then the observation is 25%.   In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended specific fungicides known to be effective against wheat yellow rust should be chosen.  When running the yellow rust model the risk for yield losses from other diseases is not considered.   If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to yellow rust. Only two categorizes are used susceptible and resistant,  if a cultivar is categorized as partly resistant, it is recommended to consider it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by yellow rust  based on scouting the crop.  Between GS  29-31 whole crop should be assessed. Between GS 32 and 71 assessments should be based only on 3 upper leaves.  Enter information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the observations  entered and update the risk.  After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific yellow rust part.   The model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_TRZAX_PUCCST',
                nodeclass='CPO_TRZAX_PUCCST',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_TRZAX_SEPTTR_CPO_TRZAX_SEPTTR = Factory(name='CPO_TRZAX_SEPTTR',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: Leaf blotch diseases of wheat can be caused by septoria tritici blotch (Zymoseptoria tritici), and Septoria nodorum blotch (Stagonospora nodorium),  which are both favoured by wet conditions.  THE DECISION: Fungicide treatments may need to be applied once or twice between stem extension (GS 32) and flowering (GS 69),  mainly to protect the upper leaves from attack of Septoria diseases.  THE MODEL: The CPO Septoria model estimates risk of septoria tritici blotch infections in winter wheat. Weather data from GS 32 to GS 69 are used.  Spraying is recommended after minimum 4 days with rain (> 1mm) in susceptible cultivars counting days between GS 32 and GS 69.  In resistant cultivars risk of attack is assumed after 5 days with rain (>1mm) between GS 37 and GS 69. Counting of days with rain goes back a maximum of 30 days.  When running the Septoria model the risk for yield losses from other diseases than Septoria is not considered.   If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to Septoria diseases. Only two categorizes are used susceptible and resistant, if a cultivar is categorized as partly resistant,  we recommend that it is considered as susceptible.  Enter the specific growth stages at the time when the crop monitoring and weather data is entered.  Enter information on the incidence of attacked plants by Septoria diseases based on scouting the crop on leaf 3 from the top. If more than 10% of 3rd leaves (F-2) are attacked  and no previous treatments have been applied against Septoria it is recommended to spray even if fewer than 4 days with precipitation has been counted.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the observations entered and update the risk.  After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nASSUMPTIONS: Septoria tritici blotch is present in the crop and periods with high humidity create risk for a damaging epidemic\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific Septoria part.   The model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_TRZAX_SEPTTR',
                nodeclass='CPO_TRZAX_SEPTTR',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_TRZAX_PUCCRE_CPO_TRZAX_PUCCRE = Factory(name='CPO_TRZAX_PUCCRE',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: Brown rust (Puccinia triticina ) is known to attack wheat\n\nTHE DECISION: Fungicide treatments may need to be applied between start of elongation  (GS 30)  and beginning of grain filling (GS 71), to protect leaves from attack of brown rust and yield losses.  THE MODEL: The CPO brown rust model is recommending treatments in wheat when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked.  The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 80 plants are completely healthy, then the observation is 25%). In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars. If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended specific fungicides known to be effective against this brown rust  should be chosen.  When running the brown rust model the risk for yield losses from other diseases is not considered.  If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \n\nTHE PARAMETERS: To obtain accurate risk predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to brown rust. Only two categories are used susceptible and resistant,  if a cultivar is categorised as partly\nresistant, it is recommended to consider it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by brown rust based on scouting the crop. Between GS 30-31 whole crop should be assessed. Between GS 32 and 65 assessments should be based only on 3 upper leaves. Enter information on last fungicide spray dates is vital for the model. This is also  done in 'Edit parameters'.  Clicking on 'Save' will keep the observations  entered and update the risk.   After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\n\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific brown rust part.   The model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_TRZAX_PUCCRE',
                nodeclass='CPO_TRZAX_PUCCRE',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_dk_seges_CPO_TRZAX_PYRNTR_CPO_TRZAX_PYRNTR = Factory(name='CPO_TRZAX_PYRNTR',
                authors='SEGES (wralea authors)',
                description=b"THE PEST: Tan spot (Pyrenophora tritici-repentis) is known to attack wheat   THE DECISION: Fungicide treatments may need to be applied between beginning of elongation (GS 31)  and beginning of grain filling (GS 71), to protect leaves from attack of tan spot and yield losses.  THE MODEL: The CPO tan spot model is recommending treatments in wheat when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked. The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%.  In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended specific fungicides known to be effective against this tan spot should be chosen.  When running the tan spot model the risk for yield losses from other diseases is not considered.   If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to tan spot. Only two categories are used susceptible and resistant, if a cultivar is categorised as partly resistant, it is recommended to consider it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by tan spot based on scouting the crop. Between GS  29-31 whole crop should be assessed.  Between GS 32 and 71 assessments should be based only on 3 upper leaves.  Enter information on last fungicide spray dates is vital for the model. This is also  done in 'Edit parameters'.  Clicking on 'Save' will keep the observations entered and update the risk.   After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific tan spot part.   The model may be of use in other countries in Northern Europe.",
                category='none',
                nodemodule='ipmdecisions.dss.dk.seges.CPO_TRZAX_PYRNTR',
                nodeclass='CPO_TRZAX_PYRNTR',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




