from openalea.dss import Manager
def MELIAE(weathersource, p1=1002, p2=1102, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Adult pollen (bronzed-blossom) beetles (Meligethes aeneus/Brassicogethes aeneus) overwinter in the soil.   The beetles become active in early spring and fly to flowering brassica crops about a month later, where they feed on  the buds and flowers.  During feeding, females chew holes in the bases of the unopened flower buds and lay eggs in each hole.   After hatching, the larvae feed initially on pollen but later feed on unopened flowers and finally on newly-formed seed pods.  The fully-grown larvae drop to the soil where they pupate.  Adult (summer) beetles emerge 2-3 weeks later and the majority disperse to feed on other plants, including the florets of cauliflower crops, before they move to overwintering sites.   There is only one generation each year.\nTHE DECISION: This model predicts the timing of spring emergence of adult beetles, egg laying and then the emergence of a new (summer)  generation of adults ready to disperse, followed by their dispersal.  This enables users to undertake targeted monitoring and/or  mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.   The model simulates the development of cohorts of 500 individuals through spring emergence, egg laying and hatching, larval and pupal  development and emergence, followed by dispersal of the new generation of adult beetles. For each stage, the percentage development is  calculated each day by integrating the appropriate development rate curve. This percentage is accumulated over days until it reaches 100. At this point the individual moves to the next stage. Variability within the insect population is incorporated by assuming that, at any instant,  the rates of development of a population held at a constant temperature are normally distributed (Phelps et al, 1993).  The model uses soil  temperatures or air temperatures depending on the stage of development. As multiple cohorts progress simultaneously, adult emergence/dispersal  and egg laying can occur at the same time.\nTHE PARAMETERS: The Pollen Beetle forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE: Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).  Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342.'
    '''
    
    h= Manager()
    _model= h.get_model("uk.WarwickHRI", "MELIAE")

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
    

