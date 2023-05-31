from openalea.dss import Manager
def ipmwiseDEMO(weathersource):
    '''    b'Adapt weed management to your needs as a professional farmer or crop advisor. Decide yourself, the level of weed control \nor let the built-in IPM principles of IPMwise guide you. The software contains useful tools to adapt the effort against weeds to the \ncurrent weed population in a field and thus minimize the use of herbicides considerably. The software can be used to plan herbicide \nefforts at both field level and as a general planning tool for crop advisors to find suitable tank mixtures and corresponding dose rates. \nThe principles of the program are based on dose response data derived from efficacy reports. In Denmark, work is currently underway to \nalso use the IPMwise decision support software in conjunction with artificial intelligence, automatic weed recognition and spray maps. \nThis demo has been restricted concerning the number of crops and weeds compared to the full Danish version.\n'
    '''
    
    h= Manager()
    _model= h.get_model("com.ipmwise", "ipmwiseDEMO")

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
    

