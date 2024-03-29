from openalea.dss import Manager
def PSILRO(weathersource, p1=1002, p2=1102, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Carrot flies (Psila rosae/Chamaepsila rosae) overwinter in the soil either as diapausing pupae or as larvae.  Late-developing insects remain as larvae and continue to feed on carrot roots throughout the winter. The insects that  overwinter as larvae form pupae during the spring.  Adult flies subsequently emerge from both types of pupae.   The female flies lay eggs in the soil close to carrot plants and, after hatching, the larvae feed on the roots and  tunnel into them, causing damage.  These larvae form pupae, which lead to the emergence of a new generation of adults. Depending on the local climate the number of carrot fly generations and their timing can differ.  When the weather is  particularly hot, carrot fly pupae may aestivate.\nTHE DECISION: The model predicts the timing of adult emergence and egg-laying throughout the year, enabling users to undertake targeted monitoring and/or mitigating actions to reduce the risk of damage to the crop.\nTHE MODEL: A series of development rate equations form the basis of the simulation model and are linked together in a program.   The model simulates the development of cohorts of 500 individuals through adult emergence, egg laying and hatching. For each stage,  the percentage development is calculated each day by integrating the appropriate development rate curve. This percentage is accumulated  over days until it reaches 100. At this point the individual moves to the next stage. Variability within the insect population is  incorporated by assuming that, at any instant, the rates of development of a population held at a constant temperature are normally  distributed (Phelps et al, 1993).  The model uses soil temperatures or air temperatures depending on the stage of development.  As multiple cohorts progress simultaneously, adult emergence and egg laying can occur at the same time.\nTHE PARAMETERS: The Carrot Fly forecast requires hourly soil temperatures at a depth of approximately 6 cm and hourly air temperatures.\nREGION: This DSS was adapted from work carried out in the UK\nASSUMPTION: The start date for the model is 1st February, as this is often the coldest period in the year.\nREFERENCE: Phelps, K., Collier, R.H., Reader, R.J. & Finch, S. (1993).   Monte Carlo simulation method for forecasting the timing of pest insect attacks.  Crop Protection 12, 335-342. Collier, R.H., Elliott, M.S. & Finch, S. (1994).   Development of the overwintering stages of the carrot fly, Psila rosae, (Diptera:Psilidae).  Bulletin of Entomological Research 84, 469-476. Collier, R.H. & Finch, S. (1996).  Field and laboratory studies on the effects of temperature on the development of the carrot fly (Psila rosae F.).  Annals of Applied Biology 128, 1-11.'
    '''
    
    h= Manager()
    _model= h.get_model("uk.WarwickHRI", "PSILRO")

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
    

