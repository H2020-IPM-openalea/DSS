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
    )
