from openalea.dss import Manager
def BlightApp(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Late blight is a fungal disease that can cause severe damage to crop foliage and can also infect the tubers. \nTHE DECISION: Fungicides are used to control late blight. Spraying time and fungicide choice are the most important factor for successful potato late blight control. The Garmmaps BlightApp support potato growers in implementing an optimized preventive potato late blight control strategy throughout the season. In addition to preventive spray applications, an alert is issued when curative- and even eradicant stop sprays are required. \nTHE MODEL: Spray advice is based on analysis of continously updated, 500 x 500  m high resolution weather data, on field level. Forecasted weather data is used to identify potential infection events in the near future. Measured weather data is used to check for gaps in the crop's protection under the actual spray schedule. The BlightApp will recommend a preventive spray application shortly before predicted infection events. A curative spray application is recommended when infection just may have occurred. Eradicant spray applications are recommended when infection may have occurred in the recent past. BlightApp also takes into account the sometimes rapid growth of a crop. Fast growth in combination with high disease pressure may require a shorter spray interval. The level of disease pressure can be increased or lowered according to the local situation. Fungicide characteristics are imported from the Euroblight fungicide table and include protectant as well as curative abilities, protection of new growth, tuber protection and rain fastness.\nTHE PARAMETERS: The DSS uses high resolution weather data, crop growth rate and local disease pressure. Crop growth and local disease pressure can be adjusted by the user.\nSOURCE: The DSS is developed by Wageningen Research and is tested in several countries and can be used accross Europe. Before using BlightApp the user needs to create an (free) account on Farmmaps, create a farm and buy the application. The costs of using BlightApp are 250\xe2\x82\xac/year."
    '''
    
    h= Manager()
    _model= h.get_model("nl.wur.LateBlight", "BlightApp")

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
    

