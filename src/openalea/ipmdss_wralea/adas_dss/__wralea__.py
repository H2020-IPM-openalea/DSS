
# This file has been generated at Wed May 31 02:30:32 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.adas.dss'

__editable__ = True
__version__ = '0.0.4'
__institutes__ = 'ADAS'
__authors__ = 'ADAS'
__description__ = 'IPM Decisions'
__url__ = 'https://app-rsk-adas-dss-dev-001.azurewebsites.net/dss'


__all__ = ['ipmdecisions_dss_adas_dss_DASGPA_DASGPA', 'ipmdecisions_dss_adas_dss_SITDMO_SITDMO', 'ipmdecisions_dss_adas_dss_MELIAE_MELIAE', 'ipmdecisions_dss_adas_dss_HAPDMA_HAPDMA', 'ipmdecisions_dss_adas_dss_CARPPO_CARPPO', 'ipmdecisions_dss_adas_dss_RHOPPA_RHOPPA', 'ipmdecisions_dss_adas_dss_PHYTIN_PHYTIN', 'ipmdecisions_dss_adas_dss_SEPTTR_SEPTTR', 'ipmdecisions_dss_adas_dss_DEROAG_Cereals_DEROAG_Cereals', 'ipmdecisions_dss_adas_dss_DEROAG_OSR_DEROAG_OSR', 'ipmdecisions_dss_adas_dss_IPMTOOL_IPMTOOL']



ipmdecisions_dss_adas_dss_DASGPA_DASGPA = Factory(name='DASGPA',
                authors='ADAS (wralea authors)',
                description=b"THE PEST: Cutworm are caterpillars of a few species of moth (e.g. Agrotis species) that feed at the base and roots of various crops. Eggs are laid in late spring, and the first three instar feed on surface vegetation, before burrowing into roots. Once they've moved into the roots, they cannot be controlled using contact treatments (e.g. insecticides). As adults continue to lay eggs in the crop, several 'batches' of larvae, at different instars, can be present in the crop. \n\nTHE DECISION: The DSS predicts the number of instar 1, 2 or 3 larval batches that could be active in the crop. When 4 or more batches are predicted, treatment is recommended to prevent high numbers of larvae moving into the crop roots.\nTHE MODEL: This model predicts the number of batches of vulnerable larvae (instar 1-3) currently active, based on first appearance of adult moth and subsequent larval development. Significant rainfall events cause high levels of mortality in larvae, which is included in the model.\nTHE PARAMETERS: The model uses a model start date is defined as the first day after 1st June where temperature exceeds 12 degrees as a default to predict adult moth arrival. Temperature (to determine growth rates) and rainfall (to determine mortality), ending on the 31st October. Any spray dates can be inputted into the model and are deemed to be 100% effective at removing cutworm from the model, but does not prevent subsequent batches.\nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, Rep. Ireland, and Denmark.\nASSUMPTION: This DSS assumes first arrival of adult moths to be 1st June; users monitoring abundance in field should edit the parameter to the correct first observation to improve accuracy.\nREFERENCE: Bowden et al. (1983) Annuls of Applied Biology 102, 29-47. https://doi.org/10.1111/j.1744-7348.1983.tb02663.x",
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.DASGPA',
                nodeclass='DASGPA',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_SITDMO_SITDMO = Factory(name='SITDMO',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Orange wheat blossom midge larvae feed on developing grains, causing grains to become small and shrivelled. They can also damage the outer grain layer (pericarp), allowing water to enter. This can make the grain vulnerable to fungal infection (e.g. fusarium and septoria) and result in premature sprouting. Seed from infected crops is also associated with poor germination. Susceptible crops are at the highest risk when adult midge emergence coincides with ear emergence, particularly growth stages 53\xe2\x80\x9359. Larvae that hatch after flowering do not develop properly and cause little damage.  \n\nTHE DECISION: The model predicts the emergence of adults and associated migration of females into vulnerable crops, when increased monitoring and/or treatment may be appropriate.\nTHE MODEL: Daily temperature (degrees Celsius) and rainfall (mm) data is used to identify emergence of Orange Wheat Blossom Midge. The model runs between the months May and June, but requires weather data from the 1st of January. The model runs in three phases: Phase 1: Temperature accumulation of 250 degree days above 3 degrees from 1st January.  Phase 2 (Low risk): Lasts until mean daily temperature reaches 13 degrees Celsius, followed by rainfall (>2mm). During Phase 1 and 2, there is a low risk of emergence. Phase 3 (Medium risk): One phase 2 is complete, temperature accumulation of 160 degree days above 7 degrees. During phase 3, there is a medium risk of emergence. Upon completion of phase 3 the risk is considered high for three days and a date of emergence is predicted, which will be reported in the platform. Multiple emergence dates are possible, leading to extended periods of high risk of emergence.\nTHE PARAMETERS: The model uses daily temperature and rainfall\nREGION: This DSS was adapted from work carried out in Belgium, and is considered to be applicable, but yet to be validated in, the UK,  Luxembourg, Netherlands, France, Germany, Denmark.\nASSUMPTIONS: This DSS assumes that the crop variety use is vulnerable to damage by orange wheat blossom midge, and that the user will interpret the risk against the vulnerability of the crop growth stage on farm.\nREFERENCE: Jocquemin et al. (2014) Crop Protection 58, 6-13. https://doi.org/10.1016/j.cropro.2013.12.021 ',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.SITDMO',
                nodeclass='SITDMO',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_MELIAE_MELIAE = Factory(name='MELIAE',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Pollen beetle (Meligethes spp.) adults are approximately 2.5 mm, metallic greenish-black. Females bite oilseed rape buds and lay their eggs inside. Adults and larvae attack buds and flowers, resulting in withered buds and reduced pod set. In oilseed rape, adult and larval feeding can lead to bud abortion and reduced pod set. However, damage rarely results in reduced yields for winter crops. Spring crops are more vulnerable, as the susceptible green/yellow bud stage often coincides with beetle migration. \n\nTHE DECISION: Oilseed rape is only vulnerable if large numbers of pollen beetle migrate into the crop during green bud stage. This DSS predicts migration into crops based on air temperature, and so can be used to evaluate risk to crop.\nTHE MODEL: Daily maximum air temperature is used to predict Migration Risk. The default value of 15 degrees celsius is used, as that is the temperature advised in the UK at which pollen beetles will fly.   \nTHE PARAMETERS: The model uses Daily maximum air temperature   \nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, Rep. Ireland, and Denmark.\nASSUMPTIONS: Only to be used during Oilseed rape growth stages 51-59. This model is a simplification of a more detailed model described in the paper below. \nREFERENCE: Ferguson et al. (2015) Pest Management Science 72, 609-317. https://doi.org/10.1002/ps.4069',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.MELIAE',
                nodeclass='MELIAE',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1004}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_HAPDMA_HAPDMA = Factory(name='HAPDMA',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Saddle gall midge (Haplodiplosis marginata) is a sporadic pest of cereals, which usually persists at low population levels. Yield loss can be caused by constricted vascular supply to the ears as a result of larval feeding and by lodging of gall-weakened stems in high winds. Pupae overwinter in the soil, from which adults emerge in the spring to lay eggs on vulnerable crops. Damage is caused by subsequent larval feeding. Once larvae have crawled under the leaf sheath,  they cannot be controlled using contact treatments (e.g. insecticides).\n\nTHE DECISION: This DSS indicates the best time to monitor crops for infestations (start of emergence). If abundance is high, and non-chemical managment options are unlikely to achieve adequate control, treatment needs to be applied before, or soon after oviposition.\nTHE MODEL: Cumulative emergence as a function of degree day accumulations described using a probit model. The model starts on the date of first rainfall on or after the 1st March and ends at the end of July. The model returns predicted proportion cumulative emergence, the associated risk and recommended action.\nTHE PARAMETERS: The model uses accumulative daily temperature (500 degree days above 0 degrees C)  \nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, and Denmark.\nTHE PARAMETERS: The model uses Daily temperature and rainfall\nASSUMPTIONS: This DSS assumes the earliest date of emergence of saddle gall midge to be after 500 day degrees. User must interpret the reported risk against the vulnerability of the crop growth stage on farm, and undertake  in field monitoring to assess the abundance of emerging adults.   \nREFERENCE: Rowley et al (2017) Crop Protection 102, 154-160. http://dx.doi.org/10.1016/j.cropro.2017.08.025',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.HAPDMA',
                nodeclass='HAPDMA',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_CARPPO_CARPPO = Factory(name='CARPPO',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Codling moth [Cydia pomonella] cause damage to fruit of apples, pears and other pome fruit. Larvae emerge from eggs laid on the surface of the fruit, and burrow inside. The surface blemish can reduce the value of fruit, internal damage renders the fruit unsellable.\n\nTHE DECISION: The DSS predicts the start of adult codling moth flight, enabling users to undertake targeted monitoring and/or mitigating actions to reduce the risk of damage to the crop. Typically interventions are more effective at the start of male flight, rather than at peak flight periods.   \nTHE MODEL: A 3-paramater non-linear regression model fits cumulative moth captures as a function of accumulated day degrees (Biofix 1st January) for all three of the male flights. The model predicts that 1st migration begins after 151 day degrees, 2nd migration begins after 673 day degrees, and 3rd migration begins after 1303 day degrees. The start of migration events are reported in the DSS warnings to the user. \nREGION: This DSS was adapted from work carried out in Greece, and is considered applicable, but not yet validated in,  Albania, Romania, Bosnia, Croatia, Italy, Macedonia, Montenegro, Portugal, San Marino, Slovenia, Slovakia, and Spain\nTHE PARAMETERS: The model uses Minimum and maximum temperature from the 1st of January.\nSOURCE: Aristotle University, Greece. \nASSUMPTIONS: There may be three flight periods in southern Europe, one or two in northern Europe. Predict flight does not relate to numbers of codling moth, or scale of damage caused.Where flight periods overlap, the highest current risk of new migration will be reported. \nREFERENCE: Damos et al. (2018) Bulletin of Insectology 71, 131-142 ',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.CARPPO',
                nodeclass='CARPPO',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1003}, {'name': 'p2', 'interface': IInt, 'value': 1004}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_RHOPPA_RHOPPA = Factory(name='RHOPPA',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Aphids can transmit barley/cereal yellow dwarf viruses (BYDV). Initially, aphids colonise relatively few crop plants. However, the second-generation tends to move away from the plant originally colonised. Controlling this generation is a key part of a BYDV management strategy.\n\nTHE DECISION: This DSS indicates the best time to monitor crops for aphids. If infestations are high, and non-chemical control options are unlikely to prevent second generation emergence, treatment should be considered to limit the spread of the virus.\nTHE MODEL: The second generation is likely to be present when the accumulated daily air temperatures, above a baseline temperature of 3\xc2\xbaC, reaches T-Sum 170. \nTHE PARAMETERS: The model uses Date of last spray application, daily temperature\nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, Rep. Ireland, and Denmark.\nASSUMPTIONS: This DSS assumes that the user will update the date of last insecticide applications. Its also assumes that no aphids found or insecticide treatment applied at 170DD, and restarts calculations. 2nd generation development time is consistent across regions.  \nREFERENCE: UK Agricultural and Horticultural Development Board (2022). https://ahdb.org.uk/bydv ',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.RHOPPA',
                nodeclass='RHOPPA',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_PHYTIN_PHYTIN = Factory(name='PHYTIN',
                authors='ADAS (wralea authors)',
                description=b"THE PEST: Potato late blight is a disease caused by a fungus-like organism (Phytophthora infestans) that spreads rapidly in the potato crop canopy and can also infect tubers. \nTHE DECISION: The model determines when weather conditions create high risk of infection, to guide targeting of fungicide treatment. \nTHE MODEL: A high risk 'Hutton Criteria' period occurs when two consecutive days have a minimum temperature of 10\xc2\xb0C, and at least six hours of relative humidity at or above 90%. \nTHE PARAMETERS: The model uses daily air temperature and humidity \nSOURCE: James Hutton institute, UK. Introduced in the UK for the 2017 season. Dancey et al. 2017 16th Euroblight workshop. \nASSUMPTIONS: The model does not account for higher temperatures or humidity which may occur under crop covers.\n",
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.PHYTIN',
                nodeclass='PHYTIN',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1001}, {'name': 'p2', 'interface': IInt, 'value': 3001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_SEPTTR_SEPTTR = Factory(name='SEPTTR',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Septoria tritici blotch (Zymoseptoria tritici) affects the leaves of wheat crops and is particularly damaging to yield when it reduces the green canopy area of the upper leaves during grain filling.   \nTHE DECISION: Fungicide treatment to protect the upper leaves may need to be applied between stem extension and ear emergence, before symptoms are visible on those leaves.  \nTHE MODEL: At stem extension (growth stage 31) the model uses over-winter weather to estimate the potential for a damaging epidemic developing during the summer. This information can support treatment decisions.  It should be considered along with other risk factors, particularly: septoria resistance of the wheat variety, sowing date, location and weather conditions during the emergence of the upper leaves.  \nTHE PARAMETERS: the model uses data on minimum temperature and rainfall over-winter.  \nSOURCE:  Rothamsted Research, UK. The model was developed, tested and published in 2009 and has not been implemented previously. te Beest et al. 2009 European Journal of Plant Pathology; te Beest et al. (2009) Plant Pathology.  \nASSUMPTIONS: The model provides an early estimate of the potential for an epidemic and should be interpreted in combination with other risk factors.\n',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.SEPTTR',
                nodeclass='SEPTTR',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1003}, {'name': 'p2', 'interface': IInt, 'value': 2001}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_DEROAG_Cereals_DEROAG_Cereals = Factory(name='DEROAG_Cereals',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Grey field slug (Deroceras reticulatum) are the most important slug pest in crops with they causing  over 95% of most slug damage. Slug damage are commonly seed hollowing before and during seed germination leading to patchy fields,  and damage continues on seedlings and young cereal shoots up to GS21. They thrive in humid conditions with large quantities of food.  In most cases, they reside in soil up to 10 cm deep and are 3 to 5 cm in length. Due to its limited food reserve, this slug feeds  more frequently under a variety of conditions. The slug can feed and reproduce year-round, regardless of whether it is below or above ground. Seedbeds with clods and plants that are direct drilled or minimally cultivated are likely to be damaged by slugs. Farming activities such as  ploughing also fail to affect them as they move back to the soil surface to cause damage. THE DECISION: Slug refuge traps should be placed in standing cereal crops or in stubble over a one-night period from May to October when weather conditions such as temperatures between 5 -25 degrees and moist soil surfaces occur. Slugs should be counted before temperatures rise and they leave refuge traps. The trapping should continue until the vulnerable stage of the crop has passed. THE THRESHOLD: Crops are considered to be at risk of economic damage where an average of four or more slugs are found per refuge trap. THE ASSESSMENT: Assessment is most effective where periods of slug activity are correctly identified; e.g. after period of wet or humid weather.  REGION:  ASSUMPTION: This depends on identifying the periods of slug activity for greater chances of trapping them REFERENCE: Glen 2005; Glen et al. 2006',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.DEROAG_Cereals',
                nodeclass='DEROAG_Cereals',
                inputs=[{'name': 'species', 'interface': ISequence, 'value': ['DEROAG']}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_DEROAG_OSR_DEROAG_OSR = Factory(name='DEROAG_OSR',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: Grey field slug (Deroceras reticulatum) are the most important slug pest in crops with they causing over 95% of most slug damage.  The most damage to oilseed rape occurs during the establishment phase (between sowing and the four true leaf stage), with leaf shredding more common than seed hollowing. They thrive in humid conditions with large quantities of food. In most cases, they reside in soil up to  10 cm deep and are 3 to 5 cm in length. Due to its limited food reserve, this slug feeds more frequently under a variety of conditions.  The slug can feed and reproduce year-round, regardless of whether it is below or above ground.  Seedbeds with clods and plants that are  direct drilled or minimally cultivated are likely to be damaged by slugs. Farming activities such as ploughing also fail to affect them  as they move back to the soil surface to cause damage. THE DECISION: Traps should be placed in standing crops or in stubble over a one-night period from May to October when weather conditions  such as temperatures between 5 -25 degrees and moist soil surfaces occur. Slugs should be counted before temperatures rise and they leave refuge traps.  The trapping should continue until the vulnerable stage of the crop has passed. THE THRESHOLD: Crops are considered to be at risk of economic damage where an average of one or more slugs are found per refuge trap. THE ASSESSMENT: Set up minimum of nine refuge traps per 20 ha (13 in fields larger than 20 ha) in a \xe2\x80\x9cW\xe2\x80\x9d pattern. Refuge traps can be made from an upturned saucer, baited with chicken layers mash. Threshold assessed based on the overall average number of slugs found per trap 24hrs after setting them. REGION:  ASSUMPTION: Assessment is most effective where periods of slug activity are correctly identified; e.g. after period of wet or humid weather.  Tracking slug abundance over time is recommended, rather than single assessments. REFERENCE: Glen 2005; Glen et al. 2006',
                category='none',
                nodemodule='ipmdecisions.dss.adas.dss.DEROAG_OSR',
                nodeclass='DEROAG_OSR',
                inputs=[{'name': 'species', 'interface': ISequence, 'value': ['DEROAG']}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_adas_dss_IPMTOOL_IPMTOOL = Factory(name='IPMTOOL',
                authors='ADAS (wralea authors)',
                description=b'THE PEST: This IPM planning tool provides information on all the major pests, weeds and diseases of many arable and outdoor horticultural crops.  THE DECISION: The user selects the crop types they grow.  The IPM Tool provides a list of the pests, weeds and diseases which affect each type of crop, together with identification guides.  The user selects the pests, weeds and diseases which are a problem on their farm. The Tool provides guidance on effective IPM  control methods for each of the pests, weeds and diseases selected.  Links are provided to independent sources of information about each method. The user can select those methods appropriate for their farming system.   An IPM crop plan is then produced, recording the IPM control methods planned.  The plan can be updated during  the crop season.  SOURCE: The IPM Tool was developed by ADAS and SRUC, in a project led by the NFU and funded by Defra. ASSUMPTIONS: The IPM Tool provides links to external sources of independent information from reputable sources, but over which the developers of the tool have no control. ',
                category=None,
                nodemodule='ipmdecisions.dss.adas.dss.IPMTOOL',
                nodeclass='IPMTOOL',
                inputs=[{'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




