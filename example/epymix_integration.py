from openalea.core.pkgmanager import PackageManager
from openalea.dss.dss_factory import dss_factory, encode_input, encode_output
import agroservices.ipm.fakers as ipm_fakers
from epymix.wralea.adaptor import ipm_SEIR
from openalea.core.node import FuncNode
from openalea.core import *
import json

pm = PackageManager()
pm.init()

factory = pm['ipmdecisions.epymix']['epymix_seir']
node = factory.instantiate()
input_mapping = {'weather_parameters': {"daily_tmin": 1003, "daily_tmax": 1004, "daily_rain": 2001},
                 'config_params': ["sowing_date", "delta_t", "rainfall_threshold", "scenario_ino", "Lx", "Ly", "Lr", "frac_inf", "inoc_init_abs", "ng_ext0_abs", "scenario_rot", "wheat_fraction"]}

ipm_model, service = dss_factory('epymix', node, factory=factory, **input_mapping)

input_data = ipm_fakers.input_data(ipm_model)

inputs = [{'name': 'sowing_date', 'interface': IStr, 'value': '2019-09-01'}, {'name': 'daily_tmin', 'interface': ISequence, 'value': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]}, {'name': 'daily_tmax', 'interface': ISequence, 'value': [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]}, {'name': 'daily_rain', 'interface': ISequence, 'value': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]}, {'name': 'delta_t', 'interface': IInt, 'value': 10}, {'name': 'rainfall_threshold', 'interface': IInt, 'value': 3}, {'name': 'scenario_ino', 'interface': IStr, 'value': 'initial_inoculum'}, {'name': 'Lx', 'interface': IInt, 'value': 1}, {'name': 'Ly', 'interface': IInt, 'value': 1}, {'name': 'Lr', 'interface': IInt, 'value': 1}, {'name': 'frac_inf', 'interface': IInt, 'value': 1}, {'name': 'inoc_init_abs', 'interface': IInt, 'value': 20000000}, {'name': 'ng_ext0_abs', 'interface': IInt, 'value': 20000}, {'name': 'scenario_rot', 'interface': IStr, 'value': 'uniform'}, {'name': 'wheat_fraction', 'interface': IFloat, 'value': 0.5}, {'name': 'day_length', 'interface': IInt, 'value': 4320}, {'name': 'alpha_ure', 'interface': IInt, 'value': 3}, {'name': 'radius_ure', 'interface': IInt, 'value': 5}, {'name': 'alpha_asco', 'interface': IInt, 'value': 3}, {'name': 'radius_asco', 'interface': IInt, 'value': 5}, {'name': 'alpha_pycnid', 'interface': IFloat, 'value': 2e-05}, {'name': 'radius_pycnid', 'interface': IInt, 'value': 5}, {'name': 't', 'interface': IInt, 'value': 250}, {'name': 'season', 'interface': IInt, 'value': 250}, {'name': 'mu_companion', 'interface': IFloat, 'value': 0.03}, {'name': 'beta_companion', 'interface': IFloat, 'value': 0.09}, {'name': 'end_companion', 'interface': IInt, 'value': 140}, {'name': 'LAI_K', 'interface': IInt, 'value': 6}, {'name': 'delta_companion', 'interface': IInt, 'value': 0}, {'name': 'disease', 'interface': IStr, 'value': 'septo'}, {'name': 'mu_wheat', 'interface': IFloat, 'value': 0.03}, {'name': 'nu', 'interface': IFloat, 'value': 0.03}, {'name': 'beta_wheat', 'interface': IFloat, 'value': 0.09}, {'name': 'end_wheat', 'interface': IInt, 'value': 140}, {'name': 'ber_wheat', 'interface': IInt, 'value': 1}, {'name': 'ber_companion', 'interface': IInt, 'value': 1}, {'name': 'h_wheat', 'interface': IInt, 'value': 1}, {'name': 'h_companion', 'interface': IInt, 'value': 1}, {'name': 'lambd', 'interface': IInt, 'value': 20}, {'name': 'delta_ei', 'interface': IInt, 'value': 5}, {'name': 's0', 'interface': IFloat, 'value': 0.0001}, {'name': 'pi_inf0', 'interface': IFloat, 'value': 0.0002}, {'name': 'rho', 'interface': IFloat, 'value': 0.002}, {'name': 'psi', 'interface': IFloat, 'value': 0.3}, {'name': 'gamma', 'interface': IInt, 'value': 0}, {'name': 'theta', 'interface': IFloat, 'value': 0.15}, {'name': 'sigma', 'interface': IInt, 'value': 45000000}, {'name': 'sigma_asco', 'interface': IInt, 'value': 9000000}, {'name': 'inf_begin', 'interface': IInt, 'value': 0}]
outputs = [{'name': 'Nsp', 'interface': 'ISequence'}, {'name': 'Pth', 'interface': 'ISequence'}, {'name': 'Poi', 'interface': 'ISequence'}, {'name': 'Sth', 'interface': 'ISequence'}, {'name': 'Sus', 'interface': 'ISequence'}, {'name': 'Lat', 'interface': 'ISequence'}, {'name': 'Ifc', 'interface': 'ISequence'}, {'name': 'Ifv', 'interface': 'ISequence'}, {'name': 'Rem', 'interface': 'ISequence'}, {'name': 'LAI', 'interface': 'ISequence'}, {'name': 'LAI_wheat', 'interface': 'ISequence'}, {'name': 'Poo', 'interface': 'ISequence'}, {'name': 'Eps', 'interface': 'ISequence'}, {'name': 'AUDPC', 'interface': 'ISequence'}, {'name': 'Scont', 'interface': 'ISequence'}]
node = FuncNode(inputs, outputs, ipm_SEIR)
node.name='epymix'

inputs = encode_input(node, input_data, input_mapping)
output_data = [node(input) for input in inputs]

resp = encode_output(node, input_data, output_data)
response = json.dumps(resp)