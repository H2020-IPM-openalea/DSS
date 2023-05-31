from openalea.dss import Manager
def CIBSEsingleday(weathersource):
    '''    b'This model calculates hourly tempertaure values based on the CIBSE model for a single day (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in the day using the CIBSE Guide A2 (1982). \nThe model then uses these predicted times aswell as minimum and maximum air tempertaures to fit the data via sinusoidal curves.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: '
    '''
    
    h= Manager()
    _model= h.get_model("adas.datamanipulation", "CIBSEsingleday")

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
    

