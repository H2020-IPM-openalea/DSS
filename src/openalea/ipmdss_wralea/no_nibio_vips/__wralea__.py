
# This file has been generated at Wed May 31 10:34:52 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.no.nibio.vips'

__editable__ = True
__version__ = '2.0'
__institutes__ = 'NIBIO'
__authors__ = 'NIBIO'
__description__ = 'VIPS'
__url__ = 'https://www.vips-landbruk.no/'


__all__ = ['openalea_ipmdss_wralea_no_nibio_vips_PSILARTEMP_PSILARTEMP', 'openalea_ipmdss_wralea_no_nibio_vips_DELIARADIC_DELIARADIC', 'openalea_ipmdss_wralea_no_nibio_vips_MAMESTRABR_MAMESTRABR', 'openalea_ipmdss_wralea_no_nibio_vips_PSILAROBSE_PSILAROBSE', 'openalea_ipmdss_wralea_no_nibio_vips_DELIARFOBS_DELIARFOBS', 'openalea_ipmdss_wralea_no_nibio_vips_NAERSTADMO_NAERSTADMO', 'openalea_ipmdss_wralea_no_nibio_vips_ALTERNARIA_ALTERNARIA', 'openalea_ipmdss_wralea_no_nibio_vips_NEGPROGMOD_NEGPROGMOD', 'openalea_ipmdss_wralea_no_nibio_vips_SEPAPIICOL_SEPAPIICOL', 'openalea_ipmdss_wralea_no_nibio_vips_BREMIALACT_BREMIALACT']



openalea_ipmdss_wralea_no_nibio_vips_PSILARTEMP_PSILARTEMP = Factory(name='PSILARTEMP',
                authors='NIBIO (wralea authors)',
                description=b'THE PEST: The first generation of adult carrot fly emerge from pupae in the soil in the spring, and lay eggs close to the base of vulnerable crops. Larvae initial feed at the surface, then tunnel into the tap root. Adults emerge mid-July and can lead to a second generation. \nTHE DECISION: Treatments may need to be applied soon after adults arrive in the crop, before larvae tunnel into the crop roots.  \nTHE MODEL: The model determines the start of the flight period for the 1st generation of carrot rust fly based on accumuleted degree-days (260 day-degrees) over a base temperature of 5\xc2\xb0C.  \nTHE PARAMETERS: The model uses daily air temperature \nSOURCE: Luke, Finland. \nASSUMPTIONS: Be aware that in areas with field covers (plastic, single or double non-woven covers, etc.) with early crops the preceding season (either on the current field or neighboring fields), the flight period can start earlier than predicted due to higher soil temperature under the covers.\nREFERENCE: Marjjula et al 2000\n',
                category='none',
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.PSILARTEMP',
                nodeclass='PSILARTEMP',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_DELIARADIC_DELIARADIC = Factory(name='DELIARADIC',
                authors='NIBIO (wralea authors)',
                description=b'THE PEST: Cabbage root fly larvae feed on the roots of brassicas, with damage being dependant on the crop type, growth stage and growing conditions. The cabbage root fly adults begin to lay eggs 5-7 days after emergence.  Newly transplanted or recently emerged crops are most at risk as the root systems are less developed. \nTHE DECISION: Treatments may need to be applied soon after adults arrive in the crop, before subsequent larvae tunnel into the crop roots.  \nTHE MODEL: The model determins the start of egg laying as 160 degree-days (day-degrees) based on soil temperature (10 cm), over a base of temperature of 4 \xc2\xb0C), OR based on the standard air temperature (2 m above the soil surface) at the same locations, egg laying starts at 210 degree days. \nTHE PARAMETERS: The model uses Daily soil OR air temperature \nSOURCE: NIBIO, Norway. \nASSUMPTIONS: Be aware that in areas with field covers (plastic, single or double non-woven covers, etc.) with early crops the preceding season (either on the current field or neighboring fields), the flight period can start earlier due to higher soil temperature under the covers. This model should be used in combination with direct observations of eggs in the field. This is due to large variability and to get an idea of the severity of attack. The model only applies for cabbage fly, not turnip fly.\n',
                category='none',
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.DELIARADIC',
                nodeclass='DELIARADIC',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 1112}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_MAMESTRABR_MAMESTRABR = Factory(name='MAMESTRABR',
                authors='NIBIO (wralea authors)',
                description=b'The model for the warning system for cabbage moth was developed by Dr. Nina Svae Johansen. \nIt is based on the minimum temperature threshold and the requirement for accumulated \nday-degrees for the different stages of the cabbage moth [CITATION Joh96 \t l 1044 ]. \nThe accumulated degree-day model calculates forecasts for development of the cabbage moth \nthrough the summer, generates warnings for the time when eggs and small larvae can be \nregistered in the field and the best time for treatment [CITATION Joh97 \t l 1044 ].\n\nNote that the model is based on temperature, it is not related to the presence or \nabsence of cabbage moth in the field. Thus, it is important to evaluate the situation in the field.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='none',
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.MAMESTRABR',
                nodeclass='MAMESTRABR',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 1112}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_PSILAROBSE_PSILAROBSE = Factory(name='PSILAROBSE',
                authors='NIBIO (wralea authors)',
                description=b'The warning system model is based on weekly observations of adult carrot rust flies captured on yellow sticky traps. The model is based in its entirety on observations, with no input of weather data or weather forecasts. Traps are placed in the field edge and in the field and are examined for carrot rust flies weekly throughout the season. The number of adult carrot rust flies is registered in VIPS and is used in the warning system model. The observations are compared with the economic threshold levels and a warning is calculated. After organophosphates (which had a good effect against larvae) were removed from the market, they were replaced by pyrethroids that only work against the adult stage. Studies were carried out in 2005 and 2006 to adjust the larval-based thresholds to chemical control of adult flies. The experience from Norway and other countries indicated that the first treatment against carrot rust flies should be done as soon as possible after the first fly is observed on the traps. The threshold that is used in VIPS is therefore at the first observation of 1 fly.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='none',
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.PSILAROBSE',
                nodeclass='PSILAROBSE',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'species', 'interface': ISequence, 'value': ['PSILRO']}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_DELIARFOBS_DELIARFOBS = Factory(name='DELIARFOBS',
                authors='NIBIO (wralea authors)',
                description=b'The warning system model is based on weekly observations of oviposition by the brassica root flies [CITATION Bli991 l 1044 ]. The model is based in its entirety on observations, with no input of weather data or weather forecasts. The model does not distinguish between the cabbage maggot and the turnip fly. The observations consist of collecting sand from the base of 10 plants and floating the eggs in water. The counts are registered in VIPS and the mean number of eggs is calculated. The observations are compared to damage thresholds [CITATION Bli99 l 1044 ] and warnings are calculated. The damage thresholds are related to the plants developmental stage and tell how many eggs that can be on a plant before there will be a reduction in growth and yield. VIPS presents two warning system models based on damage thresholds: one for newly planted cabbage and one for cabbage that has been in the field more than 4 weeks. The model can also be set up as a private warning for the farmer\xe2\x80\x99s own field, in which case the model will vary between the two different damage thresholds based on the age of the cabbage crop (starting at the time of planting). The warning system model is only valid for cabbage, cauliflower and broccoli. The damage threshold for cabbage, cauliflower and broccoli the first 4 weeks after planting is 14 eggs per plant per week. After 4 weeks the damage threshold changes to 40 eggs per plant per week. Damage thresholds have not been determined for other crucifers.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category=None,
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.DELIARFOBS',
                nodeclass='DELIARFOBS',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'species', 'interface': ISequence, 'value': ['HYLERA', 'HYLEFL']}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_NAERSTADMO_NAERSTADMO = Factory(name='NAERSTADMO',
                authors='NIBIO (wralea authors)',
                description=b'THE PEST: Potato late blight is caused by Phytophthora infestans, a fungus-like microorganism that causes the most devastating disease of potato. It spreads rapidly in the canopy, and can also infect tubers\nTHE DECISION: Protective fungicide treatments are needed to protect the crop when conditions for infection are favorable\nTHE MODEL: The model predicts if there are favorable conditions for spore production and the following conditions for spread, survival and infection of these spores. The model produces an infection risk, where a value of 2.5 is the threshold where a warning is issued.\nTHE PARAMETERS: The model uses temperature, humidity, precipitation, wind, radiation, leaf wetness and vapor pressure deficit as input parameters\nSOURCE: Developed by NIBIO in Norway \nASSUMPTIONS: Spores of potato late blight are present\nReference: Hjelkrem et al. 2021. https://doi.org/10.1016/j.ecolmodel.2021.109565\n',
                category=None,
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.NAERSTADMO',
                nodeclass='NAERSTADMO',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 2001}, {'name': 'p3', 'interface': IInt, 'value': 5001}, {'name': 'p4', 'interface': IInt, 'value': 3002}, {'name': 'p5', 'interface': IInt, 'value': 3101}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_ALTERNARIA_ALTERNARIA = Factory(name='ALTERNARIA',
                authors='NIBIO (wralea authors)',
                description=b'THE PEST: Alternaria sp cause disease on a lot of horticultural crops, and leaf spots are among the most common symptoms. \nTHE DECISION: Fungicide treatments may be needed to protect the crop when symptoms have been observed, and conditions are favourable for pathogen spread and infection\nTHE MODEL: TOMCAST is a weather-based model, derived from a model originally developed for leaf spot diseases in tomato. The model calculates daily risk values (DSV: Disease Severity Values) based on temperature and leaf wetness the previous day. DSV represents the risk of attack of early blight the previous 24 hours. Daily values of DSV are accumulated until a threshold value (adjustable) is reached, and treatment is recommended. When a spray is performed and entered into the model, accumulation of DSV is reset and starts over at 0.\nTHE PARAMETERS: The model uses temperature and leaf wetness as input parameters\nSOURCE: Based on the dew sub model of FAST (Madden et al., 1978), originally targeted at predicting early blight, Septoria leaf spot and anthracnose on tomatoes (Gleason et al., 1995). Tested and adapted to be used against early blight (Alternaria solani) in potato in Denmark (Abuley and Nielsen, 2017).\nASSUMPTIONS: \nREFERENZ: \nGleason, M.L., Macnab, A.A., Pitblado, R.E., Ricker, M.D., East, D.A., Latin, R.X., 1995. Disease warning systems for processing tomatoes in eastern North America: are we there yet? Plant Dis. 79, 113-121.\nMadden, L., Pennypacker, S.P., Macnab, A.A., 1978. Fast, a forecast system for Alternaria Solani on tomato. Phytopathology 68, 1354-1358. \nAbuley, I.K., Nielsen, B. J. 2017. Evaluation of models to control potato early blight (Alternaria solani) in Denmark. Crop Protection, 102, 118-128.',
                category=None,
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.ALTERNARIA',
                nodeclass='ALTERNARIA',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 3101}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_NEGPROGMOD_NEGPROGMOD = Factory(name='NEGPROGMOD',
                authors='NIBIO (wralea authors)',
                description=b"THE PEST: Potato late blight, caused by the fungus-like organism Phytophthora infestans causes severe damage to the foliage and can infect the tubers at harvest. THE DECISION: The model is designed to guide the timing of the first late blight fungicide application, when used in combination with other agronomic risk factors.  THE MODEL: The model uses weather data to estimate the 'epidemic free' period ('negative prognosis') by calculating the accumulated blight risk from the date of crop emergence. The model guides the first spray timing at the end of the 'epidemic free' period.  THE PARAMETERS: From the date of crop emergence, daily risk values are accumulated based on weather data (temperature, relative humidity and precipitation). The risk is an accumulated value of how the weather affects late blight germination/infection, sporulation and growth. All processes are corrected for inhibition due to drying. After the accumulated risk has reached certain thresholds, there is likely to be moderate or high blight risk.  SOURCE: The model was first introduced by Schrodter and Ullrich in Germany in the 1970s and has been widely used in Europe since.   ASSUMPTIONS: The model is based on weather data.  Other agronomic factors, such as time of row closure, cultivar susceptibility, the presence or absence of blight inoculum sources, are not included in the risk estimate. It is not applicable to potatoes grown under protection.   REFERENCE: After the original paper by Ullrich, J. & Schr\xc3\xb6dter, H. (1966), the negative prognosis model was tested in other countries (e.g. by Taylor M. C. 2003 in the UK) and was commonly combined with other models to guide subsequent fungicide applications.  Combined models, such as NegFry, have been tested in many countries, e.g. by Hansen J. G. et al., 1995 in Denmark; ",
                category=None,
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.NEGPROGMOD',
                nodeclass='NEGPROGMOD',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 2001}, {'name': 'p3', 'interface': IInt, 'value': 3002}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_SEPAPIICOL_SEPAPIICOL = Factory(name='SEPAPIICOL',
                authors='NIBIO (wralea authors)',
                description=b'THE PEST: Septoria apiicola is the cause of late blight of celery and celeriac.  Leaf spots with characteristic small dark pycnidia form on leaves and stems. \n\nTHE DECISION: If inoculum is present, symptoms can be expected to appear 7-14 days after predicted infection risk. It is recommended to intensify field inspections after periods of risk alerts.\n\nTHE MODEL: This model is based on a calculation of how leaf wetness periods influence infection of celery by Septoria apiicola in susceptible host plants.\n\nTHE PARAMETERS: Forecasts of infection risk are given after a minimum of 12 consecutive hours of leaf wetness. \nSOURCE: The model is developed in Michigan, USA and published by Lacy, 1994.\n\nASSUMPTIONS: In Norway, the model is recommended used as a guidance for field inspections for early detection of symptoms. It is generally assumed that this model has additional relevance for Septoria petroselini in parsley.\nReference: Lacy, 1994. Influence of wetness periods on infection of celery by Septoria apiicola and use in timing sprays for control. Plant Disease 1994 78, 975-979, https://www.cabdirect.org/cabdirect/abstract/19952304511 \n\n',
                category=None,
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.SEPAPIICOL',
                nodeclass='SEPAPIICOL',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 3101}, {'name': 'p2', 'interface': IInt, 'value': 1002}, {'name': 'p3', 'interface': IInt, 'value': 2001}, {'name': 'p4', 'interface': IInt, 'value': 3002}, {'name': 'species', 'interface': ISequence, 'value': ['SEPTAP']}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_no_nibio_vips_BREMIALACT_BREMIALACT = Factory(name='BREMIALACT',
                authors='NIBIO (wralea authors)',
                description=b"THE PEST: Lettuce downy mildew (Bremia lactucae) is a disease caused by a fungus-like organism (oomycete). Symptoms are light green to yellow angular lesions, with a white mass of spores favoured by wet conditions. \nTHE DECISION: In the event of a risk alert, the potential need for fungicide sprays should be assessed based on the relevant lettuce varieties' resistance to downy mildew and the time interval from previous treatments. \n\nThe MODEL: The model indicates risk of Bremia lactucae infections in lettuce crops based on climatic conditions. Criteria for both sporulation and infection need to fulfilled before a risk period is calculated. Sporulation requires high relative humidity at night. Infection will require free moisture in the following day.  \nTHE PARAMETERS: leaf wetness, relative humidity, global radiation, maximum temperature,\nSOURCE: The model is based on studies from California, US (Scherm et al 1995, Scherm and van Bruggen, 1995, Wu et al 2002), with adaptations to fit Norwegian conditions\nREFERENCE: Nordskog, B. (2006). Studies on the epidemiology of lettuce downy mildew (Bremia lactucae Regel), including a survey of fungal pathogens in field lettuce (Lactuca sativa L.) in Norway. Norwegian University of Life Sciences. PhD Thesis 2006:24.\nE: ",
                category='none',
                nodemodule='openalea.ipmdss_wralea.no_nibio_vips.BREMIALACT',
                nodeclass='BREMIALACT',
                inputs=[{'name': 'WeatherSource', 'value': None}, {'name': 'p1', 'interface': IInt, 'value': 1004}, {'name': 'p2', 'interface': IInt, 'value': 3103}, {'name': 'p3', 'interface': IInt, 'value': 5001}, {'name': 'p4', 'interface': IInt, 'value': 3002}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




