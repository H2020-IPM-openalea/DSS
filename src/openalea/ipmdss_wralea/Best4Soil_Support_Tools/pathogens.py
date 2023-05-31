from openalea.dss import Manager
def pathogens(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Soil-borne pathogens can cause serious damage to crop yield and quality. Major groups of such pathogens are: Fusarium, Phoma, Phomopsis, Phytophthora, Pythium, Rhizoctonia and Sclerotinia. Soil-borne pathogens can often be managed by crop rotations, as they infect only certain crop species and usually decline in the absence of a host crop.  A rotation containing non-host crops or varieties can lower infestation rates in the soil. THE MODEL: The model databases contain information about susceptibility and tolerance of 70 crops to 135 pathogens. PARAMETERS: The model uses crops, including green manure crops, and crop rotation. This farm specific input has to be provided by the user. SOURCE: Created by H2020 project Best4Soil, analogue to the Dutch model www.aaltjesschema.nl, developed by Wageningen University and Research. ASSUMPTIONS: The model gives risk information, assuming that the user selected plant pathogens are present in the field. At the moment, the databases are neither soil-specific, nor country-specific. This means that the crop schemes are identical for different soil types and countries. At this moment there is insufficient country-specific information on host status and sensitivity to crop damage per crop to make the database country-specific. The same is the case for soil type specific information. Because soil type plays a role in the occurrence of  soil pathogens, the soil type selection button has been built in to enable soil type specific schemes in the future. '
    '''
    
    h= Manager()
    _model= h.get_model("Best4Soil.Support.Tools", "pathogens")

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
    

