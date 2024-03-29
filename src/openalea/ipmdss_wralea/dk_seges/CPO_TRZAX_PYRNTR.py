from openalea.dss import Manager
def CPO_TRZAX_PYRNTR(weathersource, p1=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Tan spot (Pyrenophora tritici-repentis) is known to attack wheat   THE DECISION: Fungicide treatments may need to be applied between beginning of elongation (GS 31)  and beginning of grain filling (GS 71), to protect leaves from attack of tan spot and yield losses.  THE MODEL: The CPO tan spot model is recommending treatments in wheat when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked. The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%.  In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended specific fungicides known to be effective against this tan spot should be chosen.  When running the tan spot model the risk for yield losses from other diseases is not considered.   If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to tan spot. Only two categories are used susceptible and resistant, if a cultivar is categorised as partly resistant, it is recommended to consider it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by tan spot based on scouting the crop. Between GS  29-31 whole crop should be assessed.  Between GS 32 and 71 assessments should be based only on 3 upper leaves.  Enter information on last fungicide spray dates is vital for the model. This is also  done in 'Edit parameters'.  Clicking on 'Save' will keep the observations entered and update the risk.   After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific tan spot part.   The model may be of use in other countries in Northern Europe."
    '''
    
    h= Manager()
    _model= h.get_model("dk.seges", "CPO_TRZAX_PYRNTR")

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
    

