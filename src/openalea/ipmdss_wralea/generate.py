from pathlib import Path
import os
from openalea.core import UserPackage, Factory, IInt, IDateTime, IStr, ISequence
from openalea.core.pkgmanager import PackageManager

from openalea.dss import Manager, Model

pm = PackageManager()
h= Manager()

catalog = h.catalog
models = h.models
pkgs = models.keys()

# Rewrite of pkg.create_user_node
def my_user_node(pkg, name, category, description,
                         inputs, outputs, dss_id, model_id):
    
        """
        Return a new user node factory
        This function create a new python module in the package directory
        The factory is added to the package
        and the package is saved.
        """

        if (name in pkg):
            raise FactoryExistsError()

        localdir = pkg.path
        print(localdir)
        classname = name.replace(' ', '_')

        # build function parameters
        ins = []
        in_names = []
        for input in inputs:
            in_name = input['name'].replace(' ', '_').lower()
            in_names.append(in_name)
            in_value = input['value']
            if in_value is not None:
                arg = '%s=%s' % (in_name, repr(in_value))
            else:
                arg = '%s' % (in_name, )
            ins.append(arg)
        in_args = ', '.join(ins)

        # build output
        out_values = ""
        return_values = []
        for output in outputs:
            arg = output['name'].replace(' ', '_').lower()
            # if an input arg is equal to an output one,
            # change its name.
            while arg in in_names:
                arg = 'out_' + arg
            out_values += '%s = None; ' % (arg, )
            return_values.append('%s' % (arg, ))

        if return_values:
            return_values = ', '.join(return_values) + ','
        # Create the module file
        # We can adapt the template to manage specific IPM execution

        code = """
    h= Manager()
    _model= h.get_model("%s", "%s")

    source = weathersource
    output = h.run_model(_model)
    ts = output['timeStart']
    te = output['timeEnd']
    interval = output['interval']
    try:
        parameters = [p1, p2, p3, p4]
    except:
        try:
            parameters = [p1, p2, p3]
        except:
            try:
                parameters = [p1, p2]
            except:
                try:
                    parameters = [p1]
                except:
                    parameters =[]
    
    loc = output.get('locationResult', [])
    long = []
    lat = []
    alt = []
    long = [d['longitude'] for d in loc]
    lat = [d['latitude'] for d in loc]
    alt = [d['altitude'] for d in loc]
        
    weather = source.data(longitude=long, latitude=lat, altitude=alt,
        timeStart=timeStart, timeEnd=timeEnd,
         parameters=parameters, 
         interval=interval, display="json")

    ds= _model.run(weatherdata=weather)
    return ds,
    """%(dss_id, model_id)
        
        my_template = u"""\
from openalea.dss import Manager
def %s(%s):
    '''\
    %s
    '''
    %s

""" % (classname, in_args, description,  code)

        module_path = os.path.join(localdir, "%s.py" % (classname))

        file = open(module_path, 'w')
        file.write(my_template)
        file.close()

        from openalea.core.node import NodeFactory

        #pkg_name = pkg.name.replace(' ', '_')
        #absolute_nodemodule = pkg_name + '.' + classname
        local = Path(localdir).name
        absolute_nodemodule = '.'.join(['openalea.ipmdss_wralea', local, classname]) 

        factory = NodeFactory(name=name,
                              category=category,
                              description=description,
                              inputs=inputs,
                              outputs=outputs,
                              nodemodule=absolute_nodemodule,
                              nodeclass=classname,
                              authors='',
                              search_path=[localdir])

        pkg.add_factory(factory)
        pkg.write()

        return factory





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
        inputs.append(dict(name="WeatherSource", value=None))
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
        
        my_user_node(package1, name=fname,
                         category=category,
                         description=description,
                         inputs=inputs,
                         outputs=(dict(name='result', interface=IStr),),
                         dss_id=pkg, model_id=mf,
                        )
        #except:
        #    print(fname+' failed')
    
    try:
        package1.write()
    except:
        print('Package %s fail'%name)

for pkg in pkgs:
    create_pkg(pkg)

  