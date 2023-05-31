from openalea.dss import Manager
def SCLESC(weathersource):
    '''    b'Sclerotinia stem rot is usually the main disease to consider during the flowering stages of oilseed rape. There are 3 main risk factors: the presence of sclerotinia inoculum (spores), warm and humid conditions, and crops in flower.\nIf spores are present and the crop is in flower, relative humidity must be above 80% and air temperatures above 7&deg;C for 23 continuous hours for the pathogen to infect the crop. This is what is predicted by the model.'
    '''
    
    h= Manager()
    _model= h.get_model("AHDB.OSR_disease_forecasts", "SCLESC")

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
    

