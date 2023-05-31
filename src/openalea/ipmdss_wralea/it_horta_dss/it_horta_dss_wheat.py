from openalea.dss import Manager
def it_horta_dss_wheat(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'Account required, charges apply. \n\nPuccinia striiformis\nTHE DECISION: Guides application of protection strategies \nTHE MODEL: The yellow stripe rust model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nPuccinia triticina\nTHE DECISION: Application of protection strategies \nTHE MODEL: The brown leaf rust model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. \n\nFusarium graminearum\nTHE DECISION: Application of protection strategies \nTHE MODEL: The fusarium head blight model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection in the field. The model also provide the probability that the amount of mycotoxins exceeds the legal limit. \n\nZymoseptoria tritici\nTHE DECISION: Application of protection strategies \nTHE MODEL: The septoria model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection of peckled leaf spot (Septoria blotch) in the field. \n\nBlumeria graminis f. sp. tritici\nTHE DECISION: Application of protection strategies \nTHE MODEL: The septoria model takes into account the main processes of the pathogen, of the environment and of the phenological stage of the plant and elaborates all the input data in order to provide information on the risk of infection of powdery mildew of wheat in the field. \n\n\nSOURCE: All models have been adapted/developed by Horta s.l.r\nhttps://www.horta-srl.it/en/\n'
    '''
    
    h= Manager()
    _model= h.get_model("it.horta.dss", "it_horta_dss_wheat")

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
    

