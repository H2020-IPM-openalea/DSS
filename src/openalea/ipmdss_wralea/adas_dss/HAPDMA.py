from openalea.dss import Manager
def HAPDMA(weathersource, p1=1002, p2=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Saddle gall midge (Haplodiplosis marginata) is a sporadic pest of cereals, which usually persists at low population levels. Yield loss can be caused by constricted vascular supply to the ears as a result of larval feeding and by lodging of gall-weakened stems in high winds. Pupae overwinter in the soil, from which adults emerge in the spring to lay eggs on vulnerable crops. Damage is caused by subsequent larval feeding. Once larvae have crawled under the leaf sheath,  they cannot be controlled using contact treatments (e.g. insecticides).\n\nTHE DECISION: This DSS indicates the best time to monitor crops for infestations (start of emergence). If abundance is high, and non-chemical managment options are unlikely to achieve adequate control, treatment needs to be applied before, or soon after oviposition.\nTHE MODEL: Cumulative emergence as a function of degree day accumulations described using a probit model. The model starts on the date of first rainfall on or after the 1st March and ends at the end of July. The model returns predicted proportion cumulative emergence, the associated risk and recommended action.\nTHE PARAMETERS: The model uses accumulative daily temperature (500 degree days above 0 degrees C)  \nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, and Denmark.\nTHE PARAMETERS: The model uses Daily temperature and rainfall\nASSUMPTIONS: This DSS assumes the earliest date of emergence of saddle gall midge to be after 500 day degrees. User must interpret the reported risk against the vulnerability of the crop growth stage on farm, and undertake  in field monitoring to assess the abundance of emerging adults.   \nREFERENCE: Rowley et al (2017) Crop Protection 102, 154-160. http://dx.doi.org/10.1016/j.cropro.2017.08.025'
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "HAPDMA")

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
    

