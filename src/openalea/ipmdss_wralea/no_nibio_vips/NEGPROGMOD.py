from openalea.dss import Manager
def NEGPROGMOD(weathersource, p1=1002, p2=2001, p3=3002, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Potato late blight, caused by the fungus-like organism Phytophthora infestans causes severe damage to the foliage and can infect the tubers at harvest. THE DECISION: The model is designed to guide the timing of the first late blight fungicide application, when used in combination with other agronomic risk factors.  THE MODEL: The model uses weather data to estimate the 'epidemic free' period ('negative prognosis') by calculating the accumulated blight risk from the date of crop emergence. The model guides the first spray timing at the end of the 'epidemic free' period.  THE PARAMETERS: From the date of crop emergence, daily risk values are accumulated based on weather data (temperature, relative humidity and precipitation). The risk is an accumulated value of how the weather affects late blight germination/infection, sporulation and growth. All processes are corrected for inhibition due to drying. After the accumulated risk has reached certain thresholds, there is likely to be moderate or high blight risk.  SOURCE: The model was first introduced by Schrodter and Ullrich in Germany in the 1970s and has been widely used in Europe since.   ASSUMPTIONS: The model is based on weather data.  Other agronomic factors, such as time of row closure, cultivar susceptibility, the presence or absence of blight inoculum sources, are not included in the risk estimate. It is not applicable to potatoes grown under protection.   REFERENCE: After the original paper by Ullrich, J. & Schr\xc3\xb6dter, H. (1966), the negative prognosis model was tested in other countries (e.g. by Taylor M. C. 2003 in the UK) and was commonly combined with other models to guide subsequent fungicide applications.  Combined models, such as NegFry, have been tested in many countries, e.g. by Hansen J. G. et al., 1995 in Denmark; "
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "NEGPROGMOD")

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
    

