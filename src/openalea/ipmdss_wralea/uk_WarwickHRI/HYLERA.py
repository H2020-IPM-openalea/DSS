from openalea.dss import Manager
def HYLERA(weathersource, p1=1002, p2=1102, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: The cabbage root fly (Delia radicum) overwinters as a pupa, in diapause.  The first generation of adult flies emerges in the spring  and mated female flies lay their eggs in the soil close to the base of brassica plants.  After hatching, the larvae feed on the roots and may tunnel into them, causing damage.  These larvae form pupae, which lead to the emergence of a new generation of adults.  Depending on the local climate the number of cabbage root fly generations and their timing can differ.  When the weather is particularly hot, cabbage root fly pupae  may aestivate.  In some areas there is an additional biotype of cabbage root fly which has an extended pupal diapause and emerges later in the spring.  We call the two biotypes \xef\xbf\xbdearly emerging\xef\xbf\xbd and \xef\xbf\xbdlate emerging\xef\xbf\xbd.  \nTHE DECISION: The model predicts the timing of adult emergence and egg-laying throughout the year, enabling users to undertake targeted monitoring  and/or mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.   The model simulates the development of cohorts of 500 individuals through adult emergence, egg laying and hatching. For each stage, the percentage development is calculated each day by integrating the appropriate development rate curve. This percentage is accumulated over days until it reaches  100. At this point the individual moves to the next stage. Variability within the insect population is incorporated by assuming that, at any instant,  the rates of development of a population held at a constant temperature are normally distributed (Phelps et al, 1993).  The model uses soil temperatures  or air temperatures depending on the stage of development. Within the model it is possible to specify the proportions of the early and late emerging biotypes  in the simulated population. As multiple cohorts progress simultaneously, adult emergence and egg laying can occur at the same time.\nTHE PARAMETERS: The Cabbage Root Fly forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE: Collier, R.H. & Finch, S. (1983).   Completion of diapause in field populations of the cabbage root fly (Delia radicum).  Entomologia experimentalis et applicata 34, 186 192. Collier, R.H. & Finch, S. (1983).   Effects of intensity and duration of low temperatures in regulating diapause development of the cabbage root fly (Delia radicum).   Entomologia experimentalis et applicata 34, 193 200. Collier, R. H. & Finch, S. (1986).  Accumulated temperatures for predicting cabbage root fly, Delia radicum (L.), (Diptera; Anthomyiidae) emergence in the spring.  Bulletin of Entomological Research 75, 395 404. Finch, S. & Collier, R.H. (1983).  Emergence of flies from overwintering populations of cabbage root fly pupae.  Ecological Entomology 8, 29 36. Finch, S. & Collier, R.H. (1983).  Emergence of flies from overwintering populations of cabbage root fly pupae.  Ecological Entomology 8, 29 36. Finch, S. & Collier, R. H. (1985).   Laboratory studies on aestivation in the cabbage root fly (Delia radicum).  Entomologia experimentalis et applicata 38, 137 143. Finch, S., Collier, R. H. & Skinner, G. (1986).  Local population differences in emergence of cabbage root flies from south west Lancashire; implications for pest forecasting and population divergence.  Ecological Entomology 11, 139 145. Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).   Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342.'
    '''
    
    h= Manager()
    _model= h.get_model("uk.WarwickHRI", "HYLERA")

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
    

