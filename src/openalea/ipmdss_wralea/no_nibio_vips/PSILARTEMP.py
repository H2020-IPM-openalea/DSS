from openalea.dss import Manager
def PSILARTEMP(weathersource, p1=1002, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: The first generation of adult carrot fly emerge from pupae in the soil in the spring, and lay eggs close to the base of vulnerable crops. Larvae initial feed at the surface, then tunnel into the tap root. Adults emerge mid-July and can lead to a second generation. \nTHE DECISION: Treatments may need to be applied soon after adults arrive in the crop, before larvae tunnel into the crop roots.  \nTHE MODEL: The model determines the start of the flight period for the 1st generation of carrot rust fly based on accumuleted degree-days (260 day-degrees) over a base temperature of 5\xc2\xb0C.  \nTHE PARAMETERS: The model uses daily air temperature \nSOURCE: Luke, Finland. \nASSUMPTIONS: Be aware that in areas with field covers (plastic, single or double non-woven covers, etc.) with early crops the preceding season (either on the current field or neighboring fields), the flight period can start earlier than predicted due to higher soil temperature under the covers.\nREFERENCE: Marjjula et al 2000\n'
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "PSILARTEMP")

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
    

