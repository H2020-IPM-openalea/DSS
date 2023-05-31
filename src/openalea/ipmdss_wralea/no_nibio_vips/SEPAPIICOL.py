from openalea.dss import Manager
def SEPAPIICOL(weathersource, p1=3101, p2=1002, p3=2001, p4=3002, species=['SEPTAP'], timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Septoria apiicola is the cause of late blight of celery and celeriac.  Leaf spots with characteristic small dark pycnidia form on leaves and stems. \n\nTHE DECISION: If inoculum is present, symptoms can be expected to appear 7-14 days after predicted infection risk. It is recommended to intensify field inspections after periods of risk alerts.\n\nTHE MODEL: This model is based on a calculation of how leaf wetness periods influence infection of celery by Septoria apiicola in susceptible host plants.\n\nTHE PARAMETERS: Forecasts of infection risk are given after a minimum of 12 consecutive hours of leaf wetness. \nSOURCE: The model is developed in Michigan, USA and published by Lacy, 1994.\n\nASSUMPTIONS: In Norway, the model is recommended used as a guidance for field inspections for early detection of symptoms. It is generally assumed that this model has additional relevance for Septoria petroselini in parsley.\nReference: Lacy, 1994. Influence of wetness periods on infection of celery by Septoria apiicola and use in timing sprays for control. Plant Disease 1994 78, 975-979, https://www.cabdirect.org/cabdirect/abstract/19952304511 \n\n'
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "SEPAPIICOL")

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
    

