from openalea.dss import Manager
def DELIARADIC(weathersource, p1=1002, p2=1112, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Cabbage root fly larvae feed on the roots of brassicas, with damage being dependant on the crop type, growth stage and growing conditions. The cabbage root fly adults begin to lay eggs 5-7 days after emergence.  Newly transplanted or recently emerged crops are most at risk as the root systems are less developed. \nTHE DECISION: Treatments may need to be applied soon after adults arrive in the crop, before subsequent larvae tunnel into the crop roots.  \nTHE MODEL: The model determins the start of egg laying as 160 degree-days (day-degrees) based on soil temperature (10 cm), over a base of temperature of 4 \xc2\xb0C), OR based on the standard air temperature (2 m above the soil surface) at the same locations, egg laying starts at 210 degree days. \nTHE PARAMETERS: The model uses Daily soil OR air temperature \nSOURCE: NIBIO, Norway. \nASSUMPTIONS: Be aware that in areas with field covers (plastic, single or double non-woven covers, etc.) with early crops the preceding season (either on the current field or neighboring fields), the flight period can start earlier due to higher soil temperature under the covers. This model should be used in combination with direct observations of eggs in the field. This is due to large variability and to get an idea of the severity of attack. The model only applies for cabbage fly, not turnip fly.\n'
    '''
    
    h= Manager()
    _model= h.get_model("no.nibio.vips", "DELIARADIC")

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
    

