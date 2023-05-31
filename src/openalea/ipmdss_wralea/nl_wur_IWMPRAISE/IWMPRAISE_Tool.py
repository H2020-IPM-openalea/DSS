from openalea.dss import Manager
def IWMPRAISE_Tool(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Perennial and annual weed infestations can lead to direct and indirect damage to a wide range of outdoor crops. \nTHE DECISION: Integrated weed management tactics may affect one or more axes in the weed life cycle. They may prevent the establishment of seedlings from the seedbank (axis 1), reduce the impact established weeds have on the crop (axis 2), or reduce the weed seed/bud return to the soil (axis 3).\nTHE IWMPRAISE TOOL: This tool supports users in identifying and understanding the IPM tools and tactics available to manage perennial and annual weeds in narrow row, broad row and perennial crops. Users can select/de-select options to identify the best approach for them. This tool is currently available in English only. \nSOURCE: The IWMPRAISE TOOL was developed as part of the EU funded Horizon 2020 IWMPRAISE (727321), 2017-2022. It is designed for use across Europe.  \nREFERENCE: Kudsk et al (2020) Outlooks on Pest Management, 31, 152-159, https://doi.org/10.1564/v31_aug_02\n '
    '''
    
    h= Manager()
    _model= h.get_model("nl.wur.IWMPRAISE", "IWMPRAISE_Tool")

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
    

