"""Mother class managing DSS catalog"""
import pandas

from agroservices.ipm.ipm import IPM
import agroservices.ipm.fakers as fakers
from openalea.dss.ipm_DSS import DSS


class Manager:
    """DSS manager allows to access IPM DSS catalog, generate DSS instances and generate DSS packages
    """

    def __init__(self):
        """[summary]
        """
        self._ipm = IPM()
        self._catalog = self._ipm.get_dss()

    @property
    def catalog(self):
        """catalog of DSS with meta informations"""
        return {k: {kk:vv for kk,vv in v.items() if kk != 'models'} for k,v in self._catalog.items()}

    @property
    def models(self):
        """ Catalog of model per dss

        Returns
        -------
        [dict]
            [dict of dss catalog with meta-information by dss and model]
        """

        return {k: v['models'] for k,v in self._catalog.items()}


    def display(self):
        """Display catalog meta information (dss, model and description)

        Returns
        -------
            [return a dataframe]
        """

        df=pandas.Series(self.models).apply(pandas.Series).stack().apply(pandas.Series)
        df=df[["pests","crops","description"]]
        df=df.reset_index()
        df.rename(columns={"level_0":"dss","level_1":"models"},inplace=True)

        return df


    def dss(self, dss_name="no.nibio.vips"):
        """Instanciate a DSS object from name

        Parameters
        ----------
        dss : str, optional
            [description], by default "no.nibio.vips"
        """

        if dss_name in self._catalog:
            meta = self.catalog[dss_name]
            models = self.models[dss_name]
            return DSS(dss_name, meta, models, self)
        else:
            raise ValueError('DSS ' + dss_name + ' not found')

    def get_model(self, dss_name, model_name):
        dss = self.dss(dss_name)
        return dss.get(model_name)

    def run_model(self, model, startDate, endDate, interval, location, weather_data_source, field_observations):
        """Run model with standardized call to ipm webservice"""
        parameters = model.parameter_codes
        weather_data = weather_data_source.data(parameters, startDate, endDate, interval,display='json' )
        field_data = field_observations.data(startDate, endDate, interval, location)
        input_data = fakers.input_data(model._model, weather_data, field_data)
        return self._ipm.run_model(model._model, input_data)

    def create_package(self,dss_name):
        """Create a visuala package for a dss, together with a python module containing
        standardized model classes"""
        dss = self.dss(dss_name)
        package_def = dss.as_package()
        module_header = """from openalea.DSS.manager import Manager
                 
        dss_manager = Manager()
        """
        module_classes = []
        model_class="""
        def {dss_name}_{model_name}(**kwargs):
            dss = dss_manager.dss({dss_name})
            model = dss.get({model_name})
            input_data = model.input_data(**kwargs)
            output_data = dss_manager._ipm.run_model(model._model, input_data)
            return model.output(output_data)
        """
        for model_name in dss.models:
            module_classes.append(model_class.format(dss_name=dss_name, model_name=model_name))

        module = module_header + '\n'.join(module_classes)
        module_name = dss_name + '.py'
        # open(module_name, 'w') as f:
        #    f.write(module)

        #TODO: create wralea from package def
        return package_def, module_name, module
