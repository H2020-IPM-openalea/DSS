from openalea.dss import Manager
def LEPTMA(weathersource):
    '''    b'Temperature and rainfall information is used to simulate the development of Leptosphaeria maculans -- a key pathogen responsible for phoma leaf spot and phoma stem canker.\nThe forecast predicts the date of the starting week when 10% of oilseed rape plants could potentially show symptoms of phoma leaf spot.'
    '''
    
    h= Manager()
    _model= h.get_model("AHDB.OSR_disease_forecasts", "LEPTMA")

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
    

