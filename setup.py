# -*- python -*-
#
#       Copyright INRIA - CIRAD - INRAe
#
#       File author(s):
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://github.com/openalea/weatherdata
#
# ==============================================================================

# ==============================================================================
from setuptools import setup, find_packages
# ==============================================================================


pkg_root_dir = 'src'
packages = [pkg for pkg in find_packages(pkg_root_dir)]
top_pkgs = [pkg for pkg in packages if len(pkg.split('.')) <= 2]
package_dir = dict([('', pkg_root_dir)] +
                   [(pkg, pkg_root_dir + "/" + pkg.replace('.', '/'))
                    for pkg in top_pkgs])

_version = {}
with open("src/openalea/dss/version.py") as fp:
    exec(fp.read(), _version)
version = _version['version']

description = 'IPM DSS Python interface'
long_description = 'Management of IPM DSS from python, and transform DSS outputs in a native and efficient Python data structure '

wraleas= """
openalea.ipmdss_wralea.pl_gov_edwin
openalea.ipmdss_wralea.no_nibio_vips
openalea.ipmdss_wralea.nl_wur_IWMPRAISE
openalea.ipmdss_wralea.adas_datamanipulation
openalea.ipmdss_wralea.com_ipmwise
openalea.ipmdss_wralea.dk_au_agro
openalea.ipmdss_wralea.slugstatus_farming_co_uk
openalea.ipmdss_wralea.Best4Soil_Support_Tools
openalea.ipmdss_wralea.AHDB_OSR_disease_forecasts
openalea.ipmdss_wralea.nl_wur_LateBlight
openalea.ipmdss_wralea.de_ISIP
openalea.ipmdss_wralea.dk_seges
openalea.ipmdss_wralea.adas_dss
openalea.ipmdss_wralea.it_horta_dss
openalea.ipmdss_wralea.gr_gaiasense_ipm
openalea.ipmdss_wralea.uk_WarwickHRI
""".split()

entries = ["dss = openalea.ipmdss_wralea"]
entries.extend(["%s = %s"%(k.split('.')[-1], k) for k in wraleas])

setup(
    name="openalea.dss",
    version=version,
    description=description,
    long_description=long_description,

    author="* Christian Fournier\n"
           "* Marc Labadie\n"
           "* Christophe Pradal\n",

    maintainer="",
    maintainer_email="",

    url="https://github.com/H2020-IPM-openalea/DSS",
    license="Cecill-C",
    keywords='openalea, DSS, weather',

    # package installation
    packages=packages,
    package_dir=package_dir,
    zip_safe=False,

    # See MANIFEST.in
    include_package_data=True,
    entry_points = {
       "wralea": entries},
    )
