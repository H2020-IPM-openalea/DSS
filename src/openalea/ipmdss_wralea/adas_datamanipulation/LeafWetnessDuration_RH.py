from openalea.dss import Manager
def LeafWetnessDuration_RH(weathersource):
    '''    b'This is a simple relative humidity (RH) threshold model for calcualtion of hourly leaf wetness duration (LWD). \nIt compares a single RH obsevation with a threshold (currently 87%) and if the observation is greater than the threshold, the hour is assumed to contribute to (LWD), so returns an hourly LWD value of 1.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: '
    '''
    
    h= Manager()
    _model= h.get_model("adas.datamanipulation", "LeafWetnessDuration_RH")

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
    

