from openalea.dss import Manager
def DELIARFOBS(weathersource, species=['HYLERA', 'HYLEFL']):
    '''    b'The warning system model is based on weekly observations of oviposition by the brassica root flies [CITATION Bli991 l 1044 ]. The model is based in its entirety on observations, with no input of weather data or weather forecasts. The model does not distinguish between the cabbage maggot and the turnip fly. The observations consist of collecting sand from the base of 10 plants and floating the eggs in water. The counts are registered in VIPS and the mean number of eggs is calculated. The observations are compared to damage thresholds [CITATION Bli99 l 1044 ] and warnings are calculated. The damage thresholds are related to the plants developmental stage and tell how many eggs that can be on a plant before there will be a reduction in growth and yield. VIPS presents two warning system models based on damage thresholds: one for newly planted cabbage and one for cabbage that has been in the field more than 4 weeks. The model can also be set up as a private warning for the farmer\xe2\x80\x99s own field, in which case the model will vary between the two different damage thresholds based on the age of the cabbage crop (starting at the time of planting). The warning system model is only valid for cabbage, cauliflower and broccoli. The damage threshold for cabbage, cauliflower and broccoli the first 4 weeks after planting is 14 eggs per plant per week. After 4 weeks the damage threshold changes to 40 eggs per plant per week. Damage thresholds have not been determined for other crucifers.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: '
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "DELIARFOBS")

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
    

