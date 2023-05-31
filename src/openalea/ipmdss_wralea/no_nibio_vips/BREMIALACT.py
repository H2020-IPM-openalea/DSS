from openalea.dss import Manager
def BREMIALACT(weathersource, p1=1004, p2=3103, p3=5001, p4=3002, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: Lettuce downy mildew (Bremia lactucae) is a disease caused by a fungus-like organism (oomycete). Symptoms are light green to yellow angular lesions, with a white mass of spores favoured by wet conditions. \nTHE DECISION: In the event of a risk alert, the potential need for fungicide sprays should be assessed based on the relevant lettuce varieties' resistance to downy mildew and the time interval from previous treatments. \n\nThe MODEL: The model indicates risk of Bremia lactucae infections in lettuce crops based on climatic conditions. Criteria for both sporulation and infection need to fulfilled before a risk period is calculated. Sporulation requires high relative humidity at night. Infection will require free moisture in the following day.  \nTHE PARAMETERS: leaf wetness, relative humidity, global radiation, maximum temperature,\nSOURCE: The model is based on studies from California, US (Scherm et al 1995, Scherm and van Bruggen, 1995, Wu et al 2002), with adaptations to fit Norwegian conditions\nREFERENCE: Nordskog, B. (2006). Studies on the epidemiology of lettuce downy mildew (Bremia lactucae Regel), including a survey of fungal pathogens in field lettuce (Lactuca sativa L.) in Norway. Norwegian University of Life Sciences. PhD Thesis 2006:24.\nE: "
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "BREMIALACT")

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
    

