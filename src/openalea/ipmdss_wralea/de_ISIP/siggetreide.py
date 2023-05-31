from openalea.dss import Manager
def siggetreide(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'With weather-based forecast models for pests and diseases, you can calculate the occurrence of pathogens and periods  of high infestation pressure. Infestation controls and recommendations from the plant protection services also inform you about the  current situation in your region. In addition, programs are available for calculating plant development and choosing the most  suitable tillage system.'
    '''
    
    h= Manager()
    _model= h.get_model("de.ISIP", "siggetreide")

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
    

