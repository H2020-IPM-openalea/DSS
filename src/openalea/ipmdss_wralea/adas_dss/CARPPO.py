from openalea.dss import Manager
def CARPPO(weathersource, p1=1003, p2=1004, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Codling moth [Cydia pomonella] cause damage to fruit of apples, pears and other pome fruit. Larvae emerge from eggs laid on the surface of the fruit, and burrow inside. The surface blemish can reduce the value of fruit, internal damage renders the fruit unsellable.\n\nTHE DECISION: The DSS predicts the start of adult codling moth flight, enabling users to undertake targeted monitoring and/or mitigating actions to reduce the risk of damage to the crop. Typically interventions are more effective at the start of male flight, rather than at peak flight periods.   \nTHE MODEL: A 3-paramater non-linear regression model fits cumulative moth captures as a function of accumulated day degrees (Biofix 1st January) for all three of the male flights. The model predicts that 1st migration begins after 151 day degrees, 2nd migration begins after 673 day degrees, and 3rd migration begins after 1303 day degrees. The start of migration events are reported in the DSS warnings to the user. \nREGION: This DSS was adapted from work carried out in Greece, and is considered applicable, but not yet validated in,  Albania, Romania, Bosnia, Croatia, Italy, Macedonia, Montenegro, Portugal, San Marino, Slovenia, Slovakia, and Spain\nTHE PARAMETERS: The model uses Minimum and maximum temperature from the 1st of January.\nSOURCE: Aristotle University, Greece. \nASSUMPTIONS: There may be three flight periods in southern Europe, one or two in northern Europe. Predict flight does not relate to numbers of codling moth, or scale of damage caused.Where flight periods overlap, the highest current risk of new migration will be reported. \nREFERENCE: Damos et al. (2018) Bulletin of Insectology 71, 131-142 '
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "CARPPO")

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
    

