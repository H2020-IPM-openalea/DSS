from openalea.dss import Manager
def CIBSEmultipledays(weathersource):
    '''    b'This model calculates hourly tempertaure values based on the CIBSE model for multiple days (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in each day using the CIBSE Guide A2 (1982). \nMaximum temperature is then linked, using a sinusoidal curve to the minimum temperature of the following day. Capping is introduced in this model whereby if the generated value is higher than the maximum temperature then it is reduced to the maximum tempertaure,\nand if lower than the minium temperature the generated value is changed to the minimum temperature.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: '
    '''
    
    h= Manager()
    _model= h.get_model("adas.datamanipulation", "CIBSEmultipledays")

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
    

