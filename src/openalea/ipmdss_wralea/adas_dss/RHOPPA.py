from openalea.dss import Manager
def RHOPPA(weathersource, p1=1001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Aphids can transmit barley/cereal yellow dwarf viruses (BYDV). Initially, aphids colonise relatively few crop plants. However, the second-generation tends to move away from the plant originally colonised. Controlling this generation is a key part of a BYDV management strategy.\n\nTHE DECISION: This DSS indicates the best time to monitor crops for aphids. If infestations are high, and non-chemical control options are unlikely to prevent second generation emergence, treatment should be considered to limit the spread of the virus.\nTHE MODEL: The second generation is likely to be present when the accumulated daily air temperatures, above a baseline temperature of 3\xc2\xbaC, reaches T-Sum 170. \nTHE PARAMETERS: The model uses Date of last spray application, daily temperature\nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, Rep. Ireland, and Denmark.\nASSUMPTIONS: This DSS assumes that the user will update the date of last insecticide applications. Its also assumes that no aphids found or insecticide treatment applied at 170DD, and restarts calculations. 2nd generation development time is consistent across regions.  \nREFERENCE: UK Agricultural and Horticultural Development Board (2022). https://ahdb.org.uk/bydv '
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "RHOPPA")

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
    

