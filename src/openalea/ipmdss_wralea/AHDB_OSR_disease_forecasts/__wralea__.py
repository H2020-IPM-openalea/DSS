
# This file has been generated at Wed May 31 02:30:32 2023

from openalea.core import *


__name__ = 'ipmdecisions.dss.AHDB.OSR_disease_forecasts'

__editable__ = True
__version__ = '1.0'
__institutes__ = 'Agriculture and Horticulture Development Board'
__authors__ = 'Agriculture and Horticulture Development Board'
__description__ = 'AHDB OSR disease forecasts'
__url__ = 'https://ahdb.org.uk/tools'


__all__ = ['ipmdecisions_dss_AHDB_OSR_disease_forecasts_SCLESC_SCLESC', 'ipmdecisions_dss_AHDB_OSR_disease_forecasts_LEPTMA_LEPTMA']



ipmdecisions_dss_AHDB_OSR_disease_forecasts_SCLESC_SCLESC = Factory(name='SCLESC',
                authors='Agriculture and Horticulture Development Board (wralea authors)',
                description=b'Sclerotinia stem rot is usually the main disease to consider during the flowering stages of oilseed rape. There are 3 main risk factors: the presence of sclerotinia inoculum (spores), warm and humid conditions, and crops in flower.\nIf spores are present and the crop is in flower, relative humidity must be above 80% and air temperatures above 7&deg;C for 23 continuous hours for the pathogen to infect the crop. This is what is predicted by the model.',
                category='sclerotinia, oilseed rape',
                nodemodule='ipmdecisions.dss.AHDB.OSR_disease_forecasts.SCLESC',
                nodeclass='SCLESC',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




ipmdecisions_dss_AHDB_OSR_disease_forecasts_LEPTMA_LEPTMA = Factory(name='LEPTMA',
                authors='Agriculture and Horticulture Development Board (wralea authors)',
                description=b'Temperature and rainfall information is used to simulate the development of Leptosphaeria maculans -- a key pathogen responsible for phoma leaf spot and phoma stem canker.\nThe forecast predicts the date of the starting week when 10% of oilseed rape plants could potentially show symptoms of phoma leaf spot.',
                category='Phoma leaf spot, phoma stem canker, Leptosphaeria maculans, oilseed rape',
                nodemodule='ipmdecisions.dss.AHDB.OSR_disease_forecasts.LEPTMA',
                nodeclass='LEPTMA',
                inputs=[],
                outputs=({'name': 'result', 'interface': IStr},),
                widgetmodule=None,
                widgetclass=None,
               )




