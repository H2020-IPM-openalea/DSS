from openalea.dss import Manager
def MAMESTRABR(weathersource, p1=1002, p2=1112, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'The model for the warning system for cabbage moth was developed by Dr. Nina Svae Johansen. \nIt is based on the minimum temperature threshold and the requirement for accumulated \nday-degrees for the different stages of the cabbage moth [CITATION Joh96 \t l 1044 ]. \nThe accumulated degree-day model calculates forecasts for development of the cabbage moth \nthrough the summer, generates warnings for the time when eggs and small larvae can be \nregistered in the field and the best time for treatment [CITATION Joh97 \t l 1044 ].\n\nNote that the model is based on temperature, it is not related to the presence or \nabsence of cabbage moth in the field. Thus, it is important to evaluate the situation in the field.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: '
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "MAMESTRABR")

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
    

