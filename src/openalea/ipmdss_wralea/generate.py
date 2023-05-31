from pathlib import Path

from openalea.core import UserPackage, Factory, IInt, IDateTime, IStr, ISequence
from openalea.core.pkgmanager import PackageManager

from openalea.dss import Manager, Model

pm = PackageManager()
h= Manager()

catalog = h.catalog
models = h.models
pkgs = models.keys()

def create_pkg(pkg):


    metainfo = dict()

    name = catalog[pkg]['id']
    pname = name.replace('.', '_')
    metainfo['version'] = catalog[pkg]['version']
    metainfo['institutes'] = catalog[pkg]['organization']['name']
    metainfo['authors'] = metainfo['institutes']
    metainfo['description'] = catalog[pkg]['name']
    metainfo['url'] = catalog[pkg]['url']
    # to fetch and resize
    # metainfo['icon'] = catalog[pkg]['logo_url']
    
    cwd = Path.cwd()
    new_dir = cwd/pname
    if not new_dir.exists():
        new_dir.mkdir()


    # Create new Package and its wralea
    package1 = UserPackage('ipmdecisions.dss.'+name, metainfo, new_dir)
    package1.write()

    # add the factories
    ms = models[pkg]
    mods = list(ms)
    for mf in mods:
        info = ms[mf]

        fname = info['id'].replace('-', '_')
        category = info['keywords']
        description = info['description'].encode('utf-8', 'ignore')
        _inputs = info['input']
        inputs = []
        if _inputs:
            if _inputs.get('weather_parameters'):
                wp = _inputs.get('weather_parameters')
                n = len(wp)
                for i in range(1,n+1):
                    inputs.append(dict(name='p%d'%i, interface=IInt, value=wp[i-1]['parameter_code']))
            
            if _inputs.get('field_observation'):
                fo = _inputs['field_observation']
                if 'species' in fo:
                    inputs.append(dict(name='species', interface=ISequence, value=fo['species']))


            if _inputs.get('weather_data_period_start'):
                tstart = _inputs['weather_data_period_start']
                inputs.append(dict(name='timeStart', interface=IDateTime, value='2022-03-01'))

            if _inputs.get('weather_data_period_end'):
                tstart = _inputs['weather_data_period_end']
                inputs.append(dict(name='timeEnd', interface=IDateTime, value='2022-08-01'))
        try:
            package1.create_user_node(name=fname,
                              category=category,
                              description=description,
                              inputs=inputs,
                              outputs=(dict(name='result', interface=IStr),),
                            )
        except:
            print(fname+' failed')
    
    try:
        package1.write()
    except:
        print('Package %s fail'%name)

for pkg in pkgs:
    create_pkg(pkg)

  