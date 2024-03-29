from openalea.dss import Manager
def ALTERNARIA(weathersource, p1=1002, p2=3101, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Alternaria sp cause disease on a lot of horticultural crops, and leaf spots are among the most common symptoms. \nTHE DECISION: Fungicide treatments may be needed to protect the crop when symptoms have been observed, and conditions are favourable for pathogen spread and infection\nTHE MODEL: TOMCAST is a weather-based model, derived from a model originally developed for leaf spot diseases in tomato. The model calculates daily risk values (DSV: Disease Severity Values) based on temperature and leaf wetness the previous day. DSV represents the risk of attack of early blight the previous 24 hours. Daily values of DSV are accumulated until a threshold value (adjustable) is reached, and treatment is recommended. When a spray is performed and entered into the model, accumulation of DSV is reset and starts over at 0.\nTHE PARAMETERS: The model uses temperature and leaf wetness as input parameters\nSOURCE: Based on the dew sub model of FAST (Madden et al., 1978), originally targeted at predicting early blight, Septoria leaf spot and anthracnose on tomatoes (Gleason et al., 1995). Tested and adapted to be used against early blight (Alternaria solani) in potato in Denmark (Abuley and Nielsen, 2017).\nASSUMPTIONS: \nREFERENZ: \nGleason, M.L., Macnab, A.A., Pitblado, R.E., Ricker, M.D., East, D.A., Latin, R.X., 1995. Disease warning systems for processing tomatoes in eastern North America: are we there yet? Plant Dis. 79, 113-121.\nMadden, L., Pennypacker, S.P., Macnab, A.A., 1978. Fast, a forecast system for Alternaria Solani on tomato. Phytopathology 68, 1354-1358. \nAbuley, I.K., Nielsen, B. J. 2017. Evaluation of models to control potato early blight (Alternaria solani) in Denmark. Crop Protection, 102, 118-128.'
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "ALTERNARIA")

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
    

