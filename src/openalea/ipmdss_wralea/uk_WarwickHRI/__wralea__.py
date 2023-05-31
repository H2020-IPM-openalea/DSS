
# This file has been generated at Wed May 31 02:30:32 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.uk.WarwickHRI'

__editable__ = True
__version__ = '0.0.1'
__institutes__ = 'University of Warwick (Warwick Crop Centre)'
__authors__ = 'University of Warwick (Warwick Crop Centre)'
__description__ = 'WarwickHRI'
__url__ = 'https://warwick.ac.uk/fac/sci/lifesci/wcc/morph'


__all__ = ['ipmdecisions_dss_uk_WarwickHRI_LAMTEQ_LAMTEQ', 'ipmdecisions_dss_uk_WarwickHRI_MELIAE_MELIAE', 'ipmdecisions_dss_uk_WarwickHRI_HYLERA_HYLERA', 'ipmdecisions_dss_uk_WarwickHRI_PSILRO_PSILRO']



ipmdecisions_dss_uk_WarwickHRI_LAMTEQ_LAMTEQ = Factory(name='LAMTEQ',
                authors='University of Warwick (Warwick Crop Centre) (wralea authors)',
                description=b'THE PEST: The Large Narcissus Fly (Merodon equestris) is a species of Hoverfly whose larvae feed on Narcissus (daffodils).  Large narcissus flies overwinter inside damaged bulbs as fully-grown larvae which move into the soil to form pupae in the spring. When they emerge, the adults lay their eggs in the soil close to narcissus bulbs. After they hatch, the larvae burrow through the soil and enter the bulbs via the basal plate. The larvae feed and grow inside the bulbs and destroy their centres.  There is only one generation each year.\nTHE DECISION: This model predicts the timing of adult emergence, egg laying and egg hatching, enabling users to undertake targeted monitoring and/or mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.  The model simulates the development of cohorts of 500 individuals through adult emergence, egg laying and hatching.  For each stage, the percentage development is calculated each day by integrating the appropriate development rate curve.  This percentage is accumulated over days until it reaches 100. At this point the individual moves to the next stage. Variability within the insect population is incorporated by assuming that, at any instant, the rates of development of a  population held at a constant temperature are normally distributed (Phelps et al, 1993).  The model uses soil temperatures  or air temperatures depending on the stage of development. As multiple cohorts progress simultaneously, adult emergence, egg  laying and/or egg hatching can occur at the same time. \nTHE PARAMETERS: The Large Narcissus Fly forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE:  Collier, R.H. & Finch, S. (1992). The effects of temperature on development of the large narcissus fly (Merodon equestris).  Annals of Applied Biology, 120, 383-390. Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).   Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342.',
                category='none',
                nodemodule='ipmdecisions.dss.uk.WarwickHRI.LAMTEQ',
                nodeclass='LAMTEQ',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 1102}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_uk_WarwickHRI_MELIAE_MELIAE = Factory(name='MELIAE',
                authors='University of Warwick (Warwick Crop Centre) (wralea authors)',
                description=b'THE PEST: Adult pollen (bronzed-blossom) beetles (Meligethes aeneus/Brassicogethes aeneus) overwinter in the soil.   The beetles become active in early spring and fly to flowering brassica crops about a month later, where they feed on  the buds and flowers.  During feeding, females chew holes in the bases of the unopened flower buds and lay eggs in each hole.   After hatching, the larvae feed initially on pollen but later feed on unopened flowers and finally on newly-formed seed pods.  The fully-grown larvae drop to the soil where they pupate.  Adult (summer) beetles emerge 2-3 weeks later and the majority disperse to feed on other plants, including the florets of cauliflower crops, before they move to overwintering sites.   There is only one generation each year.\nTHE DECISION: This model predicts the timing of spring emergence of adult beetles, egg laying and then the emergence of a new (summer)  generation of adults ready to disperse, followed by their dispersal.  This enables users to undertake targeted monitoring and/or  mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.   The model simulates the development of cohorts of 500 individuals through spring emergence, egg laying and hatching, larval and pupal  development and emergence, followed by dispersal of the new generation of adult beetles. For each stage, the percentage development is  calculated each day by integrating the appropriate development rate curve. This percentage is accumulated over days until it reaches 100. At this point the individual moves to the next stage. Variability within the insect population is incorporated by assuming that, at any instant,  the rates of development of a population held at a constant temperature are normally distributed (Phelps et al, 1993).  The model uses soil  temperatures or air temperatures depending on the stage of development. As multiple cohorts progress simultaneously, adult emergence/dispersal  and egg laying can occur at the same time.\nTHE PARAMETERS: The Pollen Beetle forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE: Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).  Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342.',
                category='none',
                nodemodule='ipmdecisions.dss.uk.WarwickHRI.MELIAE',
                nodeclass='MELIAE',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 1102}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_uk_WarwickHRI_HYLERA_HYLERA = Factory(name='HYLERA',
                authors='University of Warwick (Warwick Crop Centre) (wralea authors)',
                description=b'THE PEST: The cabbage root fly (Delia radicum) overwinters as a pupa, in diapause.  The first generation of adult flies emerges in the spring  and mated female flies lay their eggs in the soil close to the base of brassica plants.  After hatching, the larvae feed on the roots and may tunnel into them, causing damage.  These larvae form pupae, which lead to the emergence of a new generation of adults.  Depending on the local climate the number of cabbage root fly generations and their timing can differ.  When the weather is particularly hot, cabbage root fly pupae  may aestivate.  In some areas there is an additional biotype of cabbage root fly which has an extended pupal diapause and emerges later in the spring.  We call the two biotypes \xef\xbf\xbdearly emerging\xef\xbf\xbd and \xef\xbf\xbdlate emerging\xef\xbf\xbd.  \nTHE DECISION: The model predicts the timing of adult emergence and egg-laying throughout the year, enabling users to undertake targeted monitoring  and/or mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.   The model simulates the development of cohorts of 500 individuals through adult emergence, egg laying and hatching. For each stage, the percentage development is calculated each day by integrating the appropriate development rate curve. This percentage is accumulated over days until it reaches  100. At this point the individual moves to the next stage. Variability within the insect population is incorporated by assuming that, at any instant,  the rates of development of a population held at a constant temperature are normally distributed (Phelps et al, 1993).  The model uses soil temperatures  or air temperatures depending on the stage of development. Within the model it is possible to specify the proportions of the early and late emerging biotypes  in the simulated population. As multiple cohorts progress simultaneously, adult emergence and egg laying can occur at the same time.\nTHE PARAMETERS: The Cabbage Root Fly forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE: Collier, R.H. & Finch, S. (1983).   Completion of diapause in field populations of the cabbage root fly (Delia radicum).  Entomologia experimentalis et applicata 34, 186 192. Collier, R.H. & Finch, S. (1983).   Effects of intensity and duration of low temperatures in regulating diapause development of the cabbage root fly (Delia radicum).   Entomologia experimentalis et applicata 34, 193 200. Collier, R. H. & Finch, S. (1986).  Accumulated temperatures for predicting cabbage root fly, Delia radicum (L.), (Diptera; Anthomyiidae) emergence in the spring.  Bulletin of Entomological Research 75, 395 404. Finch, S. & Collier, R.H. (1983).  Emergence of flies from overwintering populations of cabbage root fly pupae.  Ecological Entomology 8, 29 36. Finch, S. & Collier, R.H. (1983).  Emergence of flies from overwintering populations of cabbage root fly pupae.  Ecological Entomology 8, 29 36. Finch, S. & Collier, R. H. (1985).   Laboratory studies on aestivation in the cabbage root fly (Delia radicum).  Entomologia experimentalis et applicata 38, 137 143. Finch, S., Collier, R. H. & Skinner, G. (1986).  Local population differences in emergence of cabbage root flies from south west Lancashire; implications for pest forecasting and population divergence.  Ecological Entomology 11, 139 145. Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).   Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342.',
                category='none',
                nodemodule='ipmdecisions.dss.uk.WarwickHRI.HYLERA',
                nodeclass='HYLERA',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 1102}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_uk_WarwickHRI_PSILRO_PSILRO = Factory(name='PSILRO',
                authors='University of Warwick (Warwick Crop Centre) (wralea authors)',
                description=b'THE PEST: Carrot flies (Psila rosae/Chamaepsila rosae) overwinter in the soil either as diapausing pupae or as larvae.  Late-developing insects remain as larvae and continue to feed on carrot roots throughout the winter. The insects that  overwinter as larvae form pupae during the spring.  Adult flies subsequently emerge from both types of pupae.   The female flies lay eggs in the soil close to carrot plants and, after hatching, the larvae feed on the roots and  tunnel into them, causing damage.  These larvae form pupae, which lead to the emergence of a new generation of adults. Depending on the local climate the number of carrot fly generations and their timing can differ.  When the weather is  particularly hot, carrot fly pupae may aestivate.\nTHE DECISION: The model predicts the timing of adult emergence and egg-laying throughout the year, enabling users to undertake targeted monitoring and/or mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.   The model simulates the development of cohorts of 500 individuals through adult emergence, egg laying and hatching. For each stage,  the percentage development is calculated each day by integrating the appropriate development rate curve. This percentage is accumulated  over days until it reaches 100. At this point the individual moves to the next stage. Variability within the insect population is  incorporated by assuming that, at any instant, the rates of development of a population held at a constant temperature are normally  distributed (Phelps et al, 1993).  The model uses soil temperatures or air temperatures depending on the stage of development.  As multiple cohorts progress simultaneously, adult emergence and egg laying can occur at the same time.\nTHE PARAMETERS: The Carrot Fly forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE: Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).   Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342. Collier, R.H., Elliott, M.S. & Finch, S. (1994).   Development of the overwintering stages of the carrot fly, Psila rosae, (Diptera:Psilidae).  Bulletin of Entomological Research 84, 469-476. Collier, R.H. & Finch, S. (1996).  Field and laboratory studies on the effects of temperature on the development of the carrot fly (Psila rosae F.).  Annals of Applied Biology 128, 1-11.',
                category='none',
                nodemodule='ipmdecisions.dss.uk.WarwickHRI.PSILRO',
                nodeclass='PSILRO',
                inputs=[{'name': 'p1', 'interface': IInt, 'value': 1002}, {'name': 'p2', 'interface': IInt, 'value': 1102}, {'name': 'timeStart', 'interface': IDateTime, 'value': '2022-03-01'}, {'name': 'timeEnd', 'interface': IDateTime, 'value': '2022-08-01'}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




