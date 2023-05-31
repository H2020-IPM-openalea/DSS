from openalea.dss import Manager
def SEPTORIAHU(weathersource, p1=2001, p2=3002, p3=3101, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Leaf blotch diseases of wheat can be caused by septoria tritici blotch (Zymoseptoria tritici) and staganospora nodorum blotch (Parastagonospora nodorum), which are both  favoured by wet conditions. \nTHE DECISION: Fungicide treatments may need to be applied between stem extension and ear emergence, mainly to protect the upper leaves.  \nTHE MODEL: Weather data from GS 31 are used. The humidity model estimates risk of septoria tritici blotch infections in winter wheat. Risk of attack is assumed after 20 hours with continuous wetness. A wet hour is defined as minimum 0,2 mm precipitation in an hour or minimum 85% relative humidity. \nTHE PARAMETERS:  Dates of key growth stages are given as default values, but these may not be correct for your location.  To obtain accurate risk predictions it is essential to click on the 'Edit parameters' button, enter the estimated dates of GS31 (first node detectable), GS32 (second node; third upper leaf emerging), GS33 (third node; second upper leaf emerging), GS37/39 (uppermost flag leaf emerging)  and GS75 (grain content milky), then click on the 'Save' button.  These estimated dates can be updated during the season as growth stages are reached. Adding information on septoria fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the spray dates entered.  After spraying, the model assumes that the crop is protected for 10 days.   \nSOURCE: Created by Aahus University and SEGES and released in Denmark in 2017. Tested in Lithuania, Norway, Sweden, Finland and Denmark in 2018 and 2019. \nASSUMPTIONS: septoria tritici blotch is present in the crop and periods with high humidity create risk for a damaging epidemic\n"
    '''
    
    h= Manager()
    _model= h.get_model("dk.seges", "SEPTORIAHU")

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
    

