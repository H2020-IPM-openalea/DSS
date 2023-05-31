
# This file has been generated at Wed May 31 09:12:11 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.adas.datamanipulation'

__editable__ = True
__version__ = '0.0.6'
__institutes__ = 'ADAS'
__authors__ = 'ADAS'
__description__ = 'Models'
__url__ = 'http://web1.adas.co.uk/adas_datamanipulation/algorithms'


__all__ = ['openalea_ipmdss_wralea_adas_datamanipulation_CIBSEsingleday_CIBSEsingleday', 'openalea_ipmdss_wralea_adas_datamanipulation_CIBSEmultipledays_CIBSEmultipledays', 'openalea_ipmdss_wralea_adas_datamanipulation_Sin14R_1singleday_Sin14R_1singleday', 'openalea_ipmdss_wralea_adas_datamanipulation_Sin14R_1multipledays_Sin14R_1multipledays', 'openalea_ipmdss_wralea_adas_datamanipulation_Hourly_RH_Hourly_RH', 'openalea_ipmdss_wralea_adas_datamanipulation_LeafWetnessDuration_RH_LeafWetnessDuration_RH', 'openalea_ipmdss_wralea_adas_datamanipulation_LeafWetnessDuration_LeafWetnessDuration']



openalea_ipmdss_wralea_adas_datamanipulation_CIBSEsingleday_CIBSEsingleday = Factory(name='CIBSEsingleday',
                authors='ADAS (wralea authors)',
                description=b'This model calculates hourly tempertaure values based on the CIBSE model for a single day (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in the day using the CIBSE Guide A2 (1982). \nThe model then uses these predicted times aswell as minimum and maximum air tempertaures to fit the data via sinusoidal curves.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='algorithm, temperature',
                nodemodule='openalea.ipmdss_wralea.adas_datamanipulation.CIBSEsingleday',
                nodeclass='CIBSEsingleday',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_adas_datamanipulation_CIBSEmultipledays_CIBSEmultipledays = Factory(name='CIBSEmultipledays',
                authors='ADAS (wralea authors)',
                description=b'This model calculates hourly tempertaure values based on the CIBSE model for multiple days (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in each day using the CIBSE Guide A2 (1982). \nMaximum temperature is then linked, using a sinusoidal curve to the minimum temperature of the following day. Capping is introduced in this model whereby if the generated value is higher than the maximum temperature then it is reduced to the maximum tempertaure,\nand if lower than the minium temperature the generated value is changed to the minimum temperature.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='algorithm, temperature',
                nodemodule='openalea.ipmdss_wralea.adas_datamanipulation.CIBSEmultipledays',
                nodeclass='CIBSEmultipledays',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_adas_datamanipulation_Sin14R_1singleday_Sin14R_1singleday = Factory(name='Sin14R_1singleday',
                authors='ADAS (wralea authors)',
                description=b'This model calculates hourly tempertaure values based on the Sin14R-1 model for a single day (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in the day, based upon sunrise and sunset times for the given location. \nSunrise and sunset times are dependent on the users inputs for latitude, longtiude and GMT offset.\nThe model assumes that maximum temperature always occured at hour 14, and minimum temperature an hour before sunrise.\nThe model then uses these predicted times aswell as minimum and maximum air tempertaures to fit the data via sinusoidal curves.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='algorithm, temperature',
                nodemodule='openalea.ipmdss_wralea.adas_datamanipulation.Sin14R_1singleday',
                nodeclass='Sin14R_1singleday',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_adas_datamanipulation_Sin14R_1multipledays_Sin14R_1multipledays = Factory(name='Sin14R_1multipledays',
                authors='ADAS (wralea authors)',
                description=b'This model calculates hourly tempertaure values based on the Sin14R-1 model for multiple days (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in each day, based upon sunrise and sunset times for the given location.\nSunrise and sunset times are dependent on the users inputs for latitude, longtiude and GMT offset.\nThe model assumes that maximum temperature always occured at hour 14, and minimum temperature an hour before sunrise. \nMaximum temperature is then linked, using a sinusoidal curve to the minimum temperature of the following day. Capping is introduced in this model whereby if the generated value is higher than the maximum temperature then it is reduced to the maximum tempertaure,\nand if lower than the minium temperature the generated value is changed to the minimum temperature. \n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='algorithm, temperature',
                nodemodule='openalea.ipmdss_wralea.adas_datamanipulation.Sin14R_1multipledays',
                nodeclass='Sin14R_1multipledays',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_adas_datamanipulation_Hourly_RH_Hourly_RH = Factory(name='Hourly_RH',
                authors='ADAS (wralea authors)',
                description=b'This model simulates hourly realtive humidity from hourly temperature (Eccel, 2012). The assumption is made that minimum temperature is a first guess estimate of dew point temperature.\nThe model then expresses relative humidity as the ratio between actual water vapour and saturation vapour.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='algorithm, relative humidity',
                nodemodule='openalea.ipmdss_wralea.adas_datamanipulation.Hourly_RH',
                nodeclass='Hourly_RH',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_adas_datamanipulation_LeafWetnessDuration_RH_LeafWetnessDuration_RH = Factory(name='LeafWetnessDuration_RH',
                authors='ADAS (wralea authors)',
                description=b'This is a simple relative humidity (RH) threshold model for calcualtion of hourly leaf wetness duration (LWD). \nIt compares a single RH obsevation with a threshold (currently 87%) and if the observation is greater than the threshold, the hour is assumed to contribute to (LWD), so returns an hourly LWD value of 1.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='algorithm',
                nodemodule='openalea.ipmdss_wralea.adas_datamanipulation.LeafWetnessDuration_RH',
                nodeclass='LeafWetnessDuration_RH',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




openalea_ipmdss_wralea_adas_datamanipulation_LeafWetnessDuration_LeafWetnessDuration = Factory(name='LeafWetnessDuration',
                authors='ADAS (wralea authors)',
                description=b'\nThis is a simple relative humidity (RH) threshold model for calcualtion of hourly leaf wetness duration (LWD). \nIt compares each RH observation in a datted (date and time (hour)) list with a threhsold (currently 87%), and if the observation exceeds the threshold, the value for the hour return is 1, 0 otherwise.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: ',
                category='algorithm',
                nodemodule='openalea.ipmdss_wralea.adas_datamanipulation.LeafWetnessDuration',
                nodeclass='LeafWetnessDuration',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




