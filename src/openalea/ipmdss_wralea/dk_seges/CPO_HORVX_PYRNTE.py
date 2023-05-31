from openalea.dss import Manager
def CPO_HORVX_PYRNTE(weathersource, p1=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: net blotch (Pyrenophora teres) is known to attack barley. \nTHE DECISION: Fungicide treatments may need to be applied between start of elongation  (GS 30)  and full flowering (GS 65), to protect leaves from attack of net blotch and yield losses. \nTHE MODEL: The CPO net blotch model is recommending treatments in barley when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked.  The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%. In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended specific fungicides known to be effective against net blotch  should be chosen.  When running the net blotch model, the risk for yield losses from other diseases is not considered.   If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to net blotch. Only two categorizes are used susceptible and resistant, if a cultivar is categorized as partly resistant, it is recommended to consider it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by net blotch based on scouting the crop. Between GS  30-31 whole plants should be assessed. Between GS 32 and 65 assessments should be based only on 3 upper leaves.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the observations entered and the model will update the risk.  After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific barley net blotch part.  This model may be of use in other countries in Northern Europe."
    '''
    
    h= Manager()
    _model= h.get_model("dk.seges", "CPO_HORVX_PYRNTE")

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
    

