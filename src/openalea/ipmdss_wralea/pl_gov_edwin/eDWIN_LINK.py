from openalea.dss import Manager
def eDWIN_LINK(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'The eDWIN "Virtual farm" allows users in Poland to obtain, collect and share information about the occurrence of pests in a given area and provides notifications about possible threats in the field.\nThe eDWIN platform, also provides access to data from about 600 meteorological stations throughout Poland, monitoring (among others) temperature, air humidity, rainfall total and intensity, atmospheric pressure and wind speed and direction.\nThe eDWIN advisory platform was created as part of the project "Internet Platform for Advisory and Decision Support in Integrated Plant Protection". \nThe platform is completely free and available to everyone on computers and as an application on mobile devices, but only currently accessible to users in Poland. \n\nhttps://www.edwin.gov.pl/euslugi/wirtualne-gospodarstwo'
    '''
    
    h= Manager()
    _model= h.get_model("pl.gov.edwin", "eDWIN_LINK")

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
    

