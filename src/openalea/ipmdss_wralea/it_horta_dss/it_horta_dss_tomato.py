from openalea.dss import Manager
def it_horta_dss_tomato(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'Account required, charges apply. \n\nPhytophthora infestans \nTHE DECISION: Guides application of protection strategies \nTHE MODEL: The tomato late blight model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nAlternaria solani\nTHE DECISION: Application of protection strategies \nTHE MODEL: The tomato early blight model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \nSOURCE: Horta 2023\n\nPseudomonas syringae ; Xanthomonas campestris\nTHE DECISION: Application of protection strategies \nTHE MODEL: The tomato bacterial speck model takes into account the main processes of P. syringae, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nXanthomonas campestris\nTHE DECISION: Application of protection strategies \nTHE MODEL: The tomato bacterial speck model takes into account the main processes of X. campestris, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nSOURCE: All models have been adapted/developed by Horta s.l.r\nhttps://www.horta-srl.it/en/\n'
    '''
    
    h= Manager()
    _model= h.get_model("it.horta.dss", "it_horta_dss_tomato")

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
    

