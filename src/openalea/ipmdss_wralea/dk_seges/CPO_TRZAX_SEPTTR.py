from openalea.dss import Manager
def CPO_TRZAX_SEPTTR(weathersource, p1=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Leaf blotch diseases of wheat can be caused by septoria tritici blotch (Zymoseptoria tritici), and Septoria nodorum blotch (Stagonospora nodorium),  which are both favoured by wet conditions.  THE DECISION: Fungicide treatments may need to be applied once or twice between stem extension (GS 32) and flowering (GS 69),  mainly to protect the upper leaves from attack of Septoria diseases.  THE MODEL: The CPO Septoria model estimates risk of septoria tritici blotch infections in winter wheat. Weather data from GS 32 to GS 69 are used.  Spraying is recommended after minimum 4 days with rain (> 1mm) in susceptible cultivars counting days between GS 32 and GS 69.  In resistant cultivars risk of attack is assumed after 5 days with rain (>1mm) between GS 37 and GS 69. Counting of days with rain goes back a maximum of 30 days.  When running the Septoria model the risk for yield losses from other diseases than Septoria is not considered.   If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If no action is recommended it is advised to revisit the crop after approximately one week to make a new evaluation of the risk. \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button and enter information on the cultivar's susceptibility to Septoria diseases. Only two categorizes are used susceptible and resistant, if a cultivar is categorized as partly resistant,  we recommend that it is considered as susceptible.  Enter the specific growth stages at the time when the crop monitoring and weather data is entered.  Enter information on the incidence of attacked plants by Septoria diseases based on scouting the crop on leaf 3 from the top. If more than 10% of 3rd leaves (F-2) are attacked  and no previous treatments have been applied against Septoria it is recommended to spray even if fewer than 4 days with precipitation has been counted.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the observations entered and update the risk.  After spraying, the model assumes that the crop is protected for 14 days if a broad spectrum fungicide has been applied.\nASSUMPTIONS: Septoria tritici blotch is present in the crop and periods with high humidity create risk for a damaging epidemic\nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific Septoria part.   The model may be of use in other countries in Northern Europe."
    '''
    
    h= Manager()
    _model= h.get_model("dk.seges", "CPO_TRZAX_SEPTTR")

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
    

