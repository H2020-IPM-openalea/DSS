
# This file has been generated at Wed May 31 10:34:52 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.com.ipmwise'

__editable__ = True
__version__ = '4'
__institutes__ = 'IPM Consult ApS'
__authors__ = 'IPM Consult ApS'
__description__ = 'IPMwise'
__url__ = 'http://www.ipmwise.dk'


__all__ = ['openalea_ipmdss_wralea_com_ipmwise_ipmwiseDK_ipmwiseDK', 'openalea_ipmdss_wralea_com_ipmwise_ipmwiseNO_ipmwiseNO', 'openalea_ipmdss_wralea_com_ipmwise_ipmwiseES_ipmwiseES', 'openalea_ipmdss_wralea_com_ipmwise_ipmwiseDEMO_ipmwiseDEMO']



openalea_ipmdss_wralea_com_ipmwise_ipmwiseDK_ipmwiseDK = Factory(name='ipmwiseDK',
                authors='IPM Consult ApS (wralea authors)',
                description=b'Dansk: Tilpas ukrudtsbek\xc3\xa6mpelsen til netop dit behov som landmand eller konsulent. Bestem selv, hvor rene dine marker skal v\xc3\xa6re - eller lad IPMwise\nguide dig, hvis du foretr\xc3\xa6kker IPM. Programmet indeholder nyttige v\xc3\xa6rkt\xc3\xb8jer, der kan hj\xc3\xa6lpe med at tilpasse indsatsen mod ukrudt til den aktuelle \nukrudtsbestand i marken og p\xc3\xa5 den m\xc3\xa5de mindske herbicidforbruget betragteligt. Programmet kan anvendes til planl\xc3\xa6gning af herbicidindsatsen p\xc3\xa5 b\xc3\xa5de\nmarkniveau og som et generelt planl\xc3\xa6gningsv\xc3\xa6rt\xc3\xb8j for planteavlskonsulenter til at finde egnede tankblandinger og tilh\xc3\xb8rende doser. Programmet\nfungerer ved hj\xc3\xa6lp af dosis-respons-data, som kommer fra effektrapporter. I Danmark arbejdes der for tiden p\xc3\xa5 ogs\xc3\xa5 at anvende programmet \ni forbindelse med kunstig intelligens, automatisk ukrudtsgenkendelse og tildelingskort.\n\nEnglish: Adapt weed management to your needs as a professional farmer or crop advisor. Decide yourself, the level of weed control \nor let the built-in IPM principles of IPMwise guide you. The program contains useful tools to adapt the effort against weeds to the \ncurrent weed population in a field and thus minimize the use of herbicides considerably. The program can be used to plan herbicide \nefforts at both field level and as a general planning tool for crop advisors to find suitable tank mixtures and corresponding dose rates. \nThe principles of the program are based on dose response data derived from efficacy reports. In Denmark, work is currently underway to \nalso use the program in conjunction with artificial intelligence, automatic weed recognition and spray maps.\n',
                category='weeds, herbicides, tank mixtures, dose, recommendation, efficacy, cost, timing, weed density, weed size, weed species, crop growthstage, autumn sown crops, spring sown crops, IPM, IWM, efficacy tables, Field-Specific Crop Management, Integrated weed control, Legislative framework, Crop Protection Online, Dose-response curves',
                nodemodule='openalea.ipmdss_wralea.com_ipmwise.ipmwiseDK',
                nodeclass='ipmwiseDK',
                inputs=[{'name': 'WeatherSource', 'value': None}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_com_ipmwise_ipmwiseNO_ipmwiseNO = Factory(name='ipmwiseNO',
                authors='IPM Consult ApS (wralea authors)',
                description=b'VIPS-Ugras 2.0 er en ny versjon av VIPS-ugras. IPM Consult har utviklet systemet og som p\xc3\xa5 dansk heter IPMwise. \nDet er tilpasset norske forhold av Norsk institutt for bio\xc3\xb8konomi (NIBIO) i samarbeid med Norsk Landbruksr\xc3\xa5dgiving (NLR). \nDet er nye beregninger og tilpasninger, men det er mye det samme innholdet som gamle VIPS-Ugras. VIPS-Ugras 2.0 krever \ninnlogging. Fordelen med innlogging er at systemet kan huske skiftene dine. Systemet er gratis i Norge. Du kan velge \xc3\xa5 \nbruke ferdig innlagte effektkrav eller velge dine egne effektkrav. For en optimal plantevernl\xc3\xb8sning for de fleste forhold \nanbefaler vi at du bruker systemets effektkrav  \n',
                category='weeds, herbicides, tank mixtures, dose, recommendation, efficacy, cost, timing, weed density, weed size, weed species, crop growthstage, autumn sown crops, spring sown crops, IPM, IWM, efficacy tables, Field-Specific Crop Management, Integrated weed control, Legislative framework, Crop Protection Online, Dose-response curves',
                nodemodule='openalea.ipmdss_wralea.com_ipmwise.ipmwiseNO',
                nodeclass='ipmwiseNO',
                inputs=[{'name': 'WeatherSource', 'value': None}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_com_ipmwise_ipmwiseES_ipmwiseES = Factory(name='ipmwiseES',
                authors='IPM Consult ApS (wralea authors)',
                description=b'Adapta tu manejo de malas hierbas a tus necesidades como un agricultor profesional o un asesor de cultivos. \nDecide por ti mismo el nivel de control de malas hierbas o utiliza el modulo basado en IPM del IPMwise para guiarte. \nCaracteristicas principales: Las herramientas integradas en IPMWise pueden asistirte en planificar y decidir \nlas mejores estrategias de control de malas hierbas en tus fincas. Puedes simular como afectan las diferentes\ncondiciones de la parcela a la necesidad de control y a las herramientas disponibles. En caso de que no tengas \nrecomendaciones especificas para controlar tus malas hierbas en un momento determinado, IPMWise te permite \nsimular si en momentos anteriores o posteriores al actual es posible controlar tus infestaciones de malas hierbas.  \n',
                category='weeds, herbicides, tank mixtures, dose, recommendation, efficacy, cost, timing, weed density, weed size, weed species, crop growthstage, autumn sown crops, spring sown crops, IPM, IWM, efficacy tables, Field-Specific Crop Management, Integrated weed control, Legislative framework, Crop Protection Online, Dose-response curves',
                nodemodule='openalea.ipmdss_wralea.com_ipmwise.ipmwiseES',
                nodeclass='ipmwiseES',
                inputs=[{'name': 'WeatherSource', 'value': None}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_com_ipmwise_ipmwiseDEMO_ipmwiseDEMO = Factory(name='ipmwiseDEMO',
                authors='IPM Consult ApS (wralea authors)',
                description=b'Adapt weed management to your needs as a professional farmer or crop advisor. Decide yourself, the level of weed control \nor let the built-in IPM principles of IPMwise guide you. The software contains useful tools to adapt the effort against weeds to the \ncurrent weed population in a field and thus minimize the use of herbicides considerably. The software can be used to plan herbicide \nefforts at both field level and as a general planning tool for crop advisors to find suitable tank mixtures and corresponding dose rates. \nThe principles of the program are based on dose response data derived from efficacy reports. In Denmark, work is currently underway to \nalso use the IPMwise decision support software in conjunction with artificial intelligence, automatic weed recognition and spray maps. \nThis demo has been restricted concerning the number of crops and weeds compared to the full Danish version.\n',
                category='weeds, herbicides, tank mixtures, dose, recommendation, efficacy, cost, timing, weed density, weed size, weed species, crop growthstage, autumn sown crops, spring sown crops, IPM, IWM, efficacy tables, Field-Specific Crop Management, Integrated weed control, Legislative framework, Crop Protection Online, Dose-response curves',
                nodemodule='openalea.ipmdss_wralea.com_ipmwise.ipmwiseDEMO',
                nodeclass='ipmwiseDEMO',
                inputs=[{'name': 'WeatherSource', 'value': None}],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




