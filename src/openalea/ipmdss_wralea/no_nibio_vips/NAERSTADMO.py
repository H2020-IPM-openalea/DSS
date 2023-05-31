from openalea.dss import Manager
def NAERSTADMO(weathersource, p1=1002, p2=2001, p3=5001, p4=3002, p5=3101, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Potato late blight is caused by Phytophthora infestans, a fungus-like microorganism that causes the most devastating disease of potato. It spreads rapidly in the canopy, and can also infect tubers\nTHE DECISION: Protective fungicide treatments are needed to protect the crop when conditions for infection are favorable\nTHE MODEL: The model predicts if there are favorable conditions for spore production and the following conditions for spread, survival and infection of these spores. The model produces an infection risk, where a value of 2.5 is the threshold where a warning is issued.\nTHE PARAMETERS: The model uses temperature, humidity, precipitation, wind, radiation, leaf wetness and vapor pressure deficit as input parameters\nSOURCE: Developed by NIBIO in Norway \nASSUMPTIONS: Spores of potato late blight are present\nReference: Hjelkrem et al. 2021. https://doi.org/10.1016/j.ecolmodel.2021.109565\n'
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "NAERSTADMO")

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
    

