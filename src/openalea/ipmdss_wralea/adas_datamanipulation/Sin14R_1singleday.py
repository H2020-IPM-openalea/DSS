from openalea.dss import Manager
def Sin14R_1singleday(weathersource):
    '''    b'This model calculates hourly tempertaure values based on the Sin14R-1 model for a single day (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in the day, based upon sunrise and sunset times for the given location. \nSunrise and sunset times are dependent on the users inputs for latitude, longtiude and GMT offset.\nThe model assumes that maximum temperature always occured at hour 14, and minimum temperature an hour before sunrise.\nThe model then uses these predicted times aswell as minimum and maximum air tempertaures to fit the data via sinusoidal curves.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: '
    '''
    
    h= Manager()
    _model= h.get_model("adas.datamanipulation", "Sin14R-1singleday")

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
    

