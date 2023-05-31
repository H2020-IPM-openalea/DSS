from openalea.dss import Manager
def MELIAE(weathersource, p1=1004, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Pollen beetle (Meligethes spp.) adults are approximately 2.5 mm, metallic greenish-black. Females bite oilseed rape buds and lay their eggs inside. Adults and larvae attack buds and flowers, resulting in withered buds and reduced pod set. In oilseed rape, adult and larval feeding can lead to bud abortion and reduced pod set. However, damage rarely results in reduced yields for winter crops. Spring crops are more vulnerable, as the susceptible green/yellow bud stage often coincides with beetle migration. \n\nTHE DECISION: Oilseed rape is only vulnerable if large numbers of pollen beetle migrate into the crop during green bud stage. This DSS predicts migration into crops based on air temperature, and so can be used to evaluate risk to crop.\nTHE MODEL: Daily maximum air temperature is used to predict Migration Risk. The default value of 15 degrees celsius is used, as that is the temperature advised in the UK at which pollen beetles will fly.   \nTHE PARAMETERS: The model uses Daily maximum air temperature   \nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, Rep. Ireland, and Denmark.\nASSUMPTIONS: Only to be used during Oilseed rape growth stages 51-59. This model is a simplification of a more detailed model described in the paper below. \nREFERENCE: Ferguson et al. (2015) Pest Management Science 72, 609-317. https://doi.org/10.1002/ps.4069'
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "MELIAE")

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
    

