from openalea.dss import Manager
def DASGPA(weathersource, p1=1002, p2=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Cutworm are caterpillars of a few species of moth (e.g. Agrotis species) that feed at the base and roots of various crops. Eggs are laid in late spring, and the first three instar feed on surface vegetation, before burrowing into roots. Once they've moved into the roots, they cannot be controlled using contact treatments (e.g. insecticides). As adults continue to lay eggs in the crop, several 'batches' of larvae, at different instars, can be present in the crop. \n\nTHE DECISION: The DSS predicts the number of instar 1, 2 or 3 larval batches that could be active in the crop. When 4 or more batches are predicted, treatment is recommended to prevent high numbers of larvae moving into the crop roots.\nTHE MODEL: This model predicts the number of batches of vulnerable larvae (instar 1-3) currently active, based on first appearance of adult moth and subsequent larval development. Significant rainfall events cause high levels of mortality in larvae, which is included in the model.\nTHE PARAMETERS: The model uses a model start date is defined as the first day after 1st June where temperature exceeds 12 degrees as a default to predict adult moth arrival. Temperature (to determine growth rates) and rainfall (to determine mortality), ending on the 31st October. Any spray dates can be inputted into the model and are deemed to be 100% effective at removing cutworm from the model, but does not prevent subsequent batches.\nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, Rep. Ireland, and Denmark.\nASSUMPTION: This DSS assumes first arrival of adult moths to be 1st June; users monitoring abundance in field should edit the parameter to the correct first observation to improve accuracy.\nREFERENCE: Bowden et al. (1983) Annuls of Applied Biology 102, 29-47. https://doi.org/10.1111/j.1744-7348.1983.tb02663.x"
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "DASGPA")

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
    

