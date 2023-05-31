from openalea.dss import Manager
def LAMTEQ(weathersource, p1=1002, p2=1102, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: The Large Narcissus Fly (Merodon equestris) is a species of Hoverfly whose larvae feed on Narcissus (daffodils).  Large narcissus flies overwinter inside damaged bulbs as fully-grown larvae which move into the soil to form pupae in the spring. When they emerge, the adults lay their eggs in the soil close to narcissus bulbs. After they hatch, the larvae burrow through the soil and enter the bulbs via the basal plate. The larvae feed and grow inside the bulbs and destroy their centres.  There is only one generation each year.\nTHE DECISION: This model predicts the timing of adult emergence, egg laying and egg hatching, enabling users to undertake targeted monitoring and/or mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.  The model simulates the development of cohorts of 500 individuals through adult emergence, egg laying and hatching.  For each stage, the percentage development is calculated each day by integrating the appropriate development rate curve.  This percentage is accumulated over days until it reaches 100. At this point the individual moves to the next stage. Variability within the insect population is incorporated by assuming that, at any instant, the rates of development of a  population held at a constant temperature are normally distributed (Phelps et al, 1993).  The model uses soil temperatures  or air temperatures depending on the stage of development. As multiple cohorts progress simultaneously, adult emergence, egg  laying and/or egg hatching can occur at the same time. \nTHE PARAMETERS: The Large Narcissus Fly forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE:  Collier, R.H. & Finch, S. (1992). The effects of temperature on development of the large narcissus fly (Merodon equestris).  Annals of Applied Biology, 120, 383-390. Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).   Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342.'
    '''
    
    h= Manager()
    _model= h.get_model("uk.WarwickHRI", "LAMTEQ")

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
    

