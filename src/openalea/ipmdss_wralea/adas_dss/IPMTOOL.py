from openalea.dss import Manager
def IPMTOOL(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: This IPM planning tool provides information on all the major pests, weeds and diseases of many arable and outdoor horticultural crops.  THE DECISION: The user selects the crop types they grow.  The IPM Tool provides a list of the pests, weeds and diseases which affect each type of crop, together with identification guides.  The user selects the pests, weeds and diseases which are a problem on their farm. The Tool provides guidance on effective IPM  control methods for each of the pests, weeds and diseases selected.  Links are provided to independent sources of information about each method. The user can select those methods appropriate for their farming system.   An IPM crop plan is then produced, recording the IPM control methods planned.  The plan can be updated during  the crop season.  SOURCE: The IPM Tool was developed by ADAS and SRUC, in a project led by the NFU and funded by Defra. ASSUMPTIONS: The IPM Tool provides links to external sources of independent information from reputable sources, but over which the developers of the tool have no control. '
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "IPMTOOL")

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
    

