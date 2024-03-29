
# This file has been generated at Fri Mar 12 11:59:04 2021

from openalea.core import *


__name__ = 'ipmdecisions.dss'

__editable__ = True
__description__ = 'DSS package containing list of DSS model'
__license__ = 'CeCILL-C'
__url__ = 'https://github.com/H2020-IPM-openalea/DSS'
__alias__ = []
__version__ = '1.0'
__authors__ = 'Marc LABADIE, Christophe Pradal, Christian Fournier, Corinne Robert'
__institutes__ = 'CIRAD/INRAE'
__icon__ = ''


__all__ = ['_151101224', '_151101280', 'openalea_dss_mini_models_contamination_risk', '_162154704', '_151101168']


_151101224 = DataFactory(name='meteo00-01.txt',
                    description='a sample meteo data',
                    editors=None,
                    includes=None,
                    )



_151101280 = CompositeNodeFactory(name='dss_model',
                             description='Risk of contamination calculate with rapilly model',
                             category='model',
                             doc='',
                             inputs=[  {  'desc': 'Path to the meteo data file',
      'interface': IFileStr,
      'name': 'data_file(Weather)',
      'value': None},
   {  'desc': 'Start date range of meteo file',
      'interface': IDateTime,
      'name': 'start(date_range)',
      'value': 1989},
   {  'desc': 'End date range of meteo file',
      'interface': IDateTime,
      'name': 'end(date_range)',
      'value': 1985}],
                             outputs=[  {  'desc': 'the number of contaminationg hours over the period',
      'interface': ISequence,
      'name': 'risk(contamination_risk)'}],
                             elt_factory={  2: ('ipmdecisions.dss', 'contamination_risk'),
   3: ('alinea.astk', 'Weather'),
   5: ('alinea.astk', 'date_range')},
                             elt_connections={  94564056031656: (3, 0, 2, 0),
   94564056031680: (2, 0, '__out__', 0),
   94564056031704: ('__in__', 1, 5, 0),
   94564056031728: ('__in__', 2, 5, 1),
   94564056031752: ('__in__', 0, 3, 0),
   94564056031776: (5, 0, 2, 1)},
                             elt_data={  2: {  'block': False,
         'caption': 'contamination_risk',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -104.40801838886425,
         'posy': 38.928395608932334,
         'priority': 0,
         'use_user_color': False,
         'user_application': False,
         'user_color': None},
   3: {  'block': False,
         'caption': 'Weather',
         'delay': 0,
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -138.7943372537687,
         'posy': -15.860077283440273,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'date_range',
         'delay': 0,
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -25.036690575205313,
         'posy': -7.419969201258212,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set([]),
                'posx': -16.960744542251625,
                'posy': -112.83355273684631,
                'priority': 0,
                'use_user_color': False,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set([]),
                 'posx': -32.5618700344552,
                 'posy': 110.84569120627239,
                 'priority': 0,
                 'use_user_color': False,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [],
   5: [(2, 'None'), (3, "'H'"), (4, "u'utc'"), (5, 'False'), (6, "u'None'")],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-104.40801838886425, 38.928395608932334],
         'useUserColor': False,
         'userColor': None},
   3: {  'position': [-138.7943372537687, -15.860077283440273],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [-25.036690575205313, -7.419969201258212],
         'useUserColor': False,
         'userColor': None},
   '__in__': {  'position': [-16.960744542251625, -112.83355273684631],
                'useUserColor': False,
                'userColor': None},
   '__out__': {  'position': [-32.5618700344552, 110.84569120627239],
                 'useUserColor': False,
                 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




openalea_dss_mini_models_contamination_risk = Factory(name='contamination_risk',
                authors=' (wralea authors)',
                description='a fake simple contamination risk',
                category='model',
                nodemodule='openalea.dss.datamanipulation',
                nodeclass='contamination_risk',
                inputs=[{'interface': None, 'name': 'weather', 'value': None, 'desc': 'a weather database'}, {'interface': IStr, 'name': 'time_sequence', 'value': None, 'desc': 'the period of interest'}],
                outputs=[{'interface': ISequence, 'name': 'risk', 'desc': 'the number of contaminationg hours over the period'}],
                widgetmodule=None,
                widgetclass=None,
               )




_162154704 = CompositeNodeFactory(name='IPM workflow',
                             description='',
                             category='workflow',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('__my package__', 'WeatherData'),
   3: ('openalea.data structure.string', 'string'),
   4: ('__my package__', 'DSSData'),
   5: ('openalea.data structure.string', 'string'),
   6: ('openalea.data structure.string', 'string'),
   7: ('openalea.data structure.string', 'string'),
   8: ('openalea.data structure.string', 'string'),
   9: ('openalea.data structure.string', 'string'),
   10: ('openalea.data structure.string', 'string'),
   11: ('openalea.data structure.string', 'string'),
   12: ('openalea.data structure.string', 'string'),
   13: ('openalea.data structure.string', 'string'),
   14: ('openalea.data structure.string', 'string'),
   15: ('openalea.data structure.string', 'string'),
   16: ('openalea.data structure.string', 'string'),
   17: ('openalea.data structure.string', 'string'),
   18: ('openalea.data structure.string', 'string'),
   19: ('openalea.data structure.string', 'string'),
   20: ('openalea.data structure.string', 'string'),
   21: ('openalea.data structure.string', 'string'),
   22: ('openalea.data structure.string', 'string'),
   23: ('openalea.flow control', 'annotation'),
   24: ('openalea.flow control', 'annotation'),
   25: ('openalea.flow control', 'annotation'),
   26: ('openalea.flow control', 'annotation'),
   27: ('openalea.flow control', 'annotation')},
                             elt_connections={  51733488: (9, 0, 11, 0),
   51733512: (12, 0, 2, 1),
   51733536: (14, 0, 2, 3),
   51733560: (16, 0, 2, 5),
   51733584: (4, 0, 5, 0),
   51733608: (17, 0, 4, 1),
   51733632: (3, 0, 17, 0),
   51733656: (8, 0, 2, 0),
   51733680: (19, 0, 2, 7),
   51733704: (22, 0, 17, 0),
   51733728: (7, 0, 6, 0),
   51733752: (11, 0, 4, 0),
   51733776: (13, 0, 2, 2),
   51733800: (15, 0, 2, 4),
   51733824: (18, 0, 2, 6),
   51733848: (2, 0, 3, 0),
   51733872: (3, 0, 22, 0),
   51733896: (9, 0, 10, 0),
   51733920: (7, 0, 8, 0),
   51733944: (20, 0, 2, 8),
   51733968: (21, 0, 4, 1)},
                             elt_data={  2: {  'block': False,
         'caption': 'WeatherData',
         'delay': 0,
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -451.4349938812333,
         'posy': -139.48555586012844,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'Weather data output',
         'delay': 0,
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -320.92445868849825,
         'posy': 14.862724698217619,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'DSSData',
         'delay': 0,
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 814.1422860004325,
         'posy': -43.036687699066924,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'model output',
         'delay': 0,
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 874.5466603226184,
         'posy': 101.92745535603942,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'list weather adapter',
         'delay': 0,
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -905.5029167488743,
         'posy': -179.03324080368657,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'WheatherHub',
         'delay': 0,
         'hide': True,
         'id': 7,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -820.1723790441533,
         'posy': -314.19932295406437,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'Name weatheradapter',
         'delay': 0,
         'hide': True,
         'id': 8,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -736.6885328184513,
         'posy': -184.14677437321146,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'DSSHub',
         'delay': 0,
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': 990.2311245586445,
         'posy': -284.7286011118634,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'list of DSS',
          'delay': 0,
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': 1153.368270061754,
          'posy': -196.87147177841996,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   11: {  'block': False,
          'caption': 'DSS name selected',
          'delay': 0,
          'hide': True,
          'id': 11,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': 867.7146191705967,
          'posy': -236.21334496827117,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': 'Parameters',
          'delay': 0,
          'hide': True,
          'id': 12,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -514.1993314663994,
          'posy': -264.174977267037,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': 'Station_ids',
          'delay': 0,
          'hide': True,
          'id': 13,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -432.2867249098026,
          'posy': -265.6657595111037,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'block': False,
          'caption': 'timeStart',
          'delay': 0,
          'hide': True,
          'id': 14,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -360.66686379453074,
          'posy': -266.20302279602515,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   15: {  'block': False,
          'caption': 'timeEnd',
          'delay': 0,
          'hide': True,
          'id': 15,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -298.8102767131304,
          'posy': -266.0198035915621,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   16: {  'block': False,
          'caption': 'timeZone',
          'delay': 0,
          'hide': True,
          'id': 16,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -245.5025466787395,
          'posy': -264.40164178439187,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   17: {  'block': False,
          'caption': 'Input_weather_data_model',
          'delay': 0,
          'hide': True,
          'id': 17,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': 655.7532957981202,
          'posy': -269.9462740844229,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   18: {  'block': False,
          'caption': 'altitude',
          'delay': 0,
          'hide': True,
          'id': 18,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -193.35481391491322,
          'posy': -261.222810787369,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   19: {  'block': False,
          'caption': 'longitude',
          'delay': 0,
          'hide': True,
          'id': 19,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -142.85333756710946,
          'posy': -264.0352033754657,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   20: {  'block': False,
          'caption': 'latitude',
          'delay': 0,
          'hide': True,
          'id': 20,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -86.30928391837783,
          'posy': -262.14221276160083,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   21: {  'block': False,
          'caption': 'Input_fieldObservation_model',
          'delay': 0,
          'hide': True,
          'id': 21,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': 802.5083147100602,
          'posy': -271.9110354309913,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   22: {  'block': False,
          'caption': 'Weather_data_manipulation',
          'delay': 0,
          'hide': True,
          'id': 22,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': 139.83072708805446,
          'posy': -251.10891976389883,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   23: {  'id': 23,
          'posx': -1.7097714094019238,
          'posy': -364.1813102026023,
          'txt': 'DataManipulation package'},
   24: {  'id': 24,
          'posx': -921.1268499521798,
          'posy': -367.21090075831677,
          'txt': 'WeatherData Package'},
   25: {  'id': 25,
          'posx': 523.622896191979,
          'posy': -362.32834334712817,
          'txt': 'cDSS package'},
   26: {  'id': 26,
          'posx': -534.858262651929,
          'posy': -325.79314370003476,
          'txt': 'Weather input'},
   27: {  'id': 27,
          'posx': 616.7421009080878,
          'posy': -304.8866318048456,
          'txt': 'DSS input modelt'},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set([]),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set([]),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [],
   4: [],
   5: [],
   6: [],
   7: [(0, "''")],
   8: [],
   9: [(0, "''")],
   10: [],
   11: [],
   12: [(0, "''")],
   13: [(0, "''")],
   14: [(0, "''")],
   15: [(0, "''")],
   16: [(0, "''")],
   17: [],
   18: [(0, "''")],
   19: [(0, "''")],
   20: [(0, "''")],
   21: [(0, "''")],
   22: [],
   23: [],
   24: [],
   25: [],
   26: [],
   27: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-451.4349938812333, -139.48555586012844], 'userColor': None, 'useUserColor': False},
   3: {'position': [-320.92445868849825, 14.862724698217619], 'userColor': None, 'useUserColor': False},
   4: {'position': [814.1422860004325, -43.036687699066924], 'userColor': None, 'useUserColor': False},
   5: {'position': [874.5466603226184, 101.92745535603942], 'userColor': None, 'useUserColor': False},
   6: {'position': [-905.5029167488743, -179.03324080368657], 'userColor': None, 'useUserColor': False},
   7: {'position': [-820.1723790441533, -314.19932295406437], 'userColor': None, 'useUserColor': False},
   8: {'position': [-736.6885328184513, -184.14677437321146], 'userColor': None, 'useUserColor': False},
   9: {'position': [990.2311245586445, -284.7286011118634], 'userColor': None, 'useUserColor': False},
   10: {'position': [1153.368270061754, -196.87147177841996], 'userColor': None, 'useUserColor': False},
   11: {'position': [867.7146191705967, -236.21334496827117], 'userColor': None, 'useUserColor': False},
   12: {'position': [-514.1993314663994, -264.174977267037], 'userColor': None, 'useUserColor': False},
   13: {'position': [-432.2867249098026, -265.6657595111037], 'userColor': None, 'useUserColor': False},
   14: {'position': [-360.66686379453074, -266.20302279602515], 'userColor': None, 'useUserColor': False},
   15: {'position': [-298.8102767131304, -266.0198035915621], 'userColor': None, 'useUserColor': False},
   16: {'position': [-245.5025466787395, -264.40164178439187], 'userColor': None, 'useUserColor': False},
   17: {'position': [655.7532957981202, -269.9462740844229], 'userColor': None, 'useUserColor': False},
   18: {'position': [-193.35481391491322, -261.222810787369], 'userColor': None, 'useUserColor': False},
   19: {'position': [-142.85333756710946, -264.0352033754657], 'userColor': None, 'useUserColor': False},
   20: {'position': [-86.30928391837783, -262.14221276160083], 'userColor': None, 'useUserColor': False},
   21: {'position': [802.5083147100602, -271.9110354309913], 'userColor': None, 'useUserColor': False},
   22: {'position': [139.83072708805446, -251.10891976389883], 'userColor': None, 'useUserColor': False},
   23: {'visualStyle': 1, 'position': [-1.7097714094019238, -364.1813102026023], 'color': [255, 85, 0], 'text': 'DataManipulation package', 'textColor': [0, 0, 0], 'rectP2': (-1, -1)},
   24: {'visualStyle': 1, 'position': [-921.1268499521798, -367.21090075831677], 'color': [255, 255, 0], 'text': 'WeatherData Package', 'textColor': None, 'rectP2': (-1, -1)},
   25: {'visualStyle': 1, 'position': [523.622896191979, -362.32834334712817], 'color': [85, 255, 255], 'text': 'cDSS package', 'textColor': None, 'rectP2': (-1, -1)},
   26: {'visualStyle': 1, 'position': [-534.858262651929, -325.79314370003476], 'color': [154, 154, 0], 'text': 'Weather input', 'textColor': None, 'rectP2': (-1, -1)},
   27: {'visualStyle': 1, 'position': [616.7421009080878, -304.8866318048456], 'color': [41, 125, 125], 'text': 'DSS input modelt', 'textColor': None, 'rectP2': (-1, -1)},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_151101168 = CompositeNodeFactory(name='dss_demo',
                             description='A demo of dss_model',
                             category='model',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('openalea.flow control', 'annotation'),
   3: ('openalea.flow control', 'annotation'),
   4: ('ipmdecisions.dss', 'meteo00-01.txt'),
   5: ('openalea.data structure.string', 'string'),
   6: ('openalea.python method', 'sum'),
   7: ('openalea.python method', 'print'),
   8: ('ipmdecisions.dss', 'dss_model'),
   9: ('openalea.data structure', 'int'),
   10: ('openalea.data structure.string', 'string'),
   11: ('openalea.flow control', 'annotation'),
   12: ('openalea.flow control', 'annotation'),
   13: ('openalea.flow control', 'annotation'),
   14: ('openalea.flow control', 'annotation')},
                             elt_connections={  94639627297192: (5, 0, 8, 1),
   94639627297216: (7, 0, 6, 0),
   94639627297240: (8, 0, 7, 0),
   94639627297264: (10, 0, 8, 2),
   94639627297288: (4, 0, 8, 0),
   94639627297312: (6, 0, 9, 0)},
                             elt_data={  2: {  'id': 2,
         'posx': -427.58412717023793,
         'posy': -70.68270242676877,
         'txt': 'Risk of contamination outputs'},
   3: {  'id': 3,
         'posx': -420.98049351531085,
         'posy': -286.03451948841206,
         'txt': 'weather inputs'},
   4: {  'block': False,
         'caption': 'meteo00-01.txt',
         'delay': 0,
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set([2]),
         'posx': -400.32554914354137,
         'posy': -211.56284073946347,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': '2000-10-01',
         'delay': 0,
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -177.46114301624485,
         'posy': -198.69580970194937,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'sum',
         'delay': 0,
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -335.46986455204694,
         'posy': 65.57297792088583,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'print',
         'delay': 0,
         'hide': True,
         'id': 7,
         'lazy': False,
         'port_hide_changed': set([]),
         'posx': -164.2384657405586,
         'posy': -20.320035395619836,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'dss_model',
         'delay': 0,
         'hide': True,
         'id': 8,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -181.7632059964705,
         'posy': -106.45975878231037,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': '46',
         'delay': 0,
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set([]),
         'posx': -329.95328612355615,
         'posy': 112.5077193447373,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': '2000-10-05',
          'delay': 0,
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set([]),
          'posx': -68.94994851807641,
          'posy': -199.77405191676417,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   11: {  'id': 11,
          'posx': -412.9184511296757,
          'posy': -241.21334755310866,
          'txt': 'weather  file'},
   12: {  'id': 12,
          'posx': -196.58494282193186,
          'posy': -241.52643836633104,
          'txt': 'Start and end date range'},
   13: {  'id': 13,
          'posx': -425.4450255101509,
          'posy': -44.01155436311903,
          'txt': 'sequence rain period'},
   14: {  'id': 14,
          'posx': -427.7268575263337,
          'posy': 16.68438096733925,
          'txt': 'Risk: Nb of contamination hour\nduring the period'},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set([]),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set([]),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [],
   3: [],
   4: [(0, 'PackageData(dss, meteo00-01.txt)'), (1, 'None'), (2, 'None')],
   5: [(0, "u'2000-10-01'")],
   6: [  (  0,
            '[0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]')],
   7: [],
   8: [],
   9: [],
   10: [(0, "u'2000-10-05'")],
   11: [],
   12: [],
   13: [],
   14: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'color': [170, 255, 255],
         'position': [-427.58412717023793, -70.68270242676877],
         'rectP2': (526.9925747016238, 226.3429772329075),
         'text': 'Risk of contamination outputs',
         'textColor': None,
         'visualStyle': 1},
   3: {  'color': [255, 170, 255],
         'position': [-420.98049351531085, -286.03451948841206],
         'rectP2': (517.9781710855451, 160.61270345241726),
         'text': 'weather inputs',
         'textColor': None,
         'visualStyle': 1},
   4: {  'position': [-400.32554914354137, -211.56284073946347],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [-177.46114301624485, -198.69580970194937],
         'useUserColor': False,
         'userColor': None},
   6: {  'position': [-335.46986455204694, 65.57297792088583],
         'useUserColor': False,
         'userColor': None},
   7: {  'position': [-164.2384657405586, -20.320035395619836],
         'useUserColor': False,
         'userColor': None},
   8: {  'position': [-181.7632059964705, -106.45975878231037],
         'useUserColor': False,
         'userColor': None},
   9: {  'position': [-329.95328612355615, 112.5077193447373],
         'useUserColor': False,
         'userColor': None},
   10: {  'position': [-68.94994851807641, -199.77405191676417],
          'useUserColor': False,
          'userColor': None},
   11: {  'color': None,
          'position': [-412.9184511296757, -241.21334755310866],
          'rectP2': (141.08235841616835, 68.8297493901503),
          'text': 'weather  file',
          'textColor': None,
          'visualStyle': 1},
   12: {  'color': None,
          'position': [-196.58494282193186, -241.52643836633104],
          'rectP2': (237.99158567908958, 77.61929943701017),
          'text': 'Start and end date range',
          'textColor': None,
          'visualStyle': 1},
   13: {  'color': None,
          'position': [-425.4450255101509, -44.01155436311903],
          'rectP2': (525.6105173292897, 57.08057406755463),
          'text': 'sequence rain period',
          'textColor': None,
          'visualStyle': 1},
   14: {  'color': None,
          'position': [-427.7268575263337, 16.68438096733925],
          'rectP2': (235.796875, 129.6062858040355),
          'text': 'Risk: Nb of contamination hour\nduring the period',
          'textColor': None,
          'visualStyle': 1},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




