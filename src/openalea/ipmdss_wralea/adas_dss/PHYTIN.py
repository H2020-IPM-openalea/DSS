from openalea.dss import Manager
def PHYTIN(weathersource, p1=1001, p2=3001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Potato late blight is a disease caused by a fungus-like organism (Phytophthora infestans) that spreads rapidly in the potato crop canopy and can also infect tubers. \nTHE DECISION: The model determines when weather conditions create high risk of infection, to guide targeting of fungicide treatment. \nTHE MODEL: A high risk 'Hutton Criteria' period occurs when two consecutive days have a minimum temperature of 10\xc2\xb0C, and at least six hours of relative humidity at or above 90%. \nTHE PARAMETERS: The model uses daily air temperature and humidity \nSOURCE: James Hutton institute, UK. Introduced in the UK for the 2017 season. Dancey et al. 2017 16th Euroblight workshop. \nASSUMPTIONS: The model does not account for higher temperatures or humidity which may occur under crop covers.\n"
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "PHYTIN")

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
    

