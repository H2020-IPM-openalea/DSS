from openalea.dss import Manager
def SlugWatch2023(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Widely present in many horticultural and arable fields, slugs can damage crops all year round. With impacts on yield and/or quality potentially severe, it is important to manage populations of key slug species. \nTHE DECISION: Management of slug infestations is most effective when targeted at periods of high slug activity. The SlugWatch forecast provides location-specific slug activity data, along with information on weather conditions, helping make informed decisions on timing and location of slug monitoring and subsequent management. \nTHE MODEL: The SlugWatch model predicts slug activity based on forecast weather conditions. \nTHE PARAMETERS: The model uses soil temperature, air temperature and rainfall. \nSOURCE: Created by CertisBelchim and developed by Farming Online Ltd. Validated in the UK and France, considered to be appropriate for use with caution in Ireland, Spain, Belgium the Netherlands, Germany, and Denmark. \nASSUMPTIONS: This model makes no prediction on actual slug abundance, only the relative risk of slug activity if they are present. In field monitoring is required to assess the actual risk to crops of high slug activity. Please refer to appropriate economic thresholds for treatment. '
    '''
    
    h= Manager()
    _model= h.get_model("slugstatus.farming.co.uk", "SlugWatch2023")

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
    

