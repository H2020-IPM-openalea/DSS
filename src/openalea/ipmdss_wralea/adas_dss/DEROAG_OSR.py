from openalea.dss import Manager
def DEROAG_OSR(weathersource, species=['DEROAG']):
    '''    b'THE PEST: Grey field slug (Deroceras reticulatum) are the most important slug pest in crops with they causing over 95% of most slug damage.  The most damage to oilseed rape occurs during the establishment phase (between sowing and the four true leaf stage), with leaf shredding more common than seed hollowing. They thrive in humid conditions with large quantities of food. In most cases, they reside in soil up to  10 cm deep and are 3 to 5 cm in length. Due to its limited food reserve, this slug feeds more frequently under a variety of conditions.  The slug can feed and reproduce year-round, regardless of whether it is below or above ground.  Seedbeds with clods and plants that are  direct drilled or minimally cultivated are likely to be damaged by slugs. Farming activities such as ploughing also fail to affect them  as they move back to the soil surface to cause damage. THE DECISION: Traps should be placed in standing crops or in stubble over a one-night period from May to October when weather conditions  such as temperatures between 5 -25 degrees and moist soil surfaces occur. Slugs should be counted before temperatures rise and they leave refuge traps.  The trapping should continue until the vulnerable stage of the crop has passed. THE THRESHOLD: Crops are considered to be at risk of economic damage where an average of one or more slugs are found per refuge trap. THE ASSESSMENT: Set up minimum of nine refuge traps per 20 ha (13 in fields larger than 20 ha) in a \xe2\x80\x9cW\xe2\x80\x9d pattern. Refuge traps can be made from an upturned saucer, baited with chicken layers mash. Threshold assessed based on the overall average number of slugs found per trap 24hrs after setting them. REGION:  ASSUMPTION: Assessment is most effective where periods of slug activity are correctly identified; e.g. after period of wet or humid weather.  Tracking slug abundance over time is recommended, rather than single assessments. REFERENCE: Glen 2005; Glen et al. 2006'
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "DEROAG_OSR")

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
    

