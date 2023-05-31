from openalea.dss import Manager
def SEPTTR(weathersource, p1=1003, p2=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Septoria tritici blotch (Zymoseptoria tritici) affects the leaves of wheat crops and is particularly damaging to yield when it reduces the green canopy area of the upper leaves during grain filling.   \nTHE DECISION: Fungicide treatment to protect the upper leaves may need to be applied between stem extension and ear emergence, before symptoms are visible on those leaves.  \nTHE MODEL: At stem extension (growth stage 31) the model uses over-winter weather to estimate the potential for a damaging epidemic developing during the summer. This information can support treatment decisions.  It should be considered along with other risk factors, particularly: septoria resistance of the wheat variety, sowing date, location and weather conditions during the emergence of the upper leaves.  \nTHE PARAMETERS: the model uses data on minimum temperature and rainfall over-winter.  \nSOURCE:  Rothamsted Research, UK. The model was developed, tested and published in 2009 and has not been implemented previously. te Beest et al. 2009 European Journal of Plant Pathology; te Beest et al. (2009) Plant Pathology.  \nASSUMPTIONS: The model provides an early estimate of the potential for an epidemic and should be interpreted in combination with other risk factors.\n'
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "SEPTTR")

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
    

