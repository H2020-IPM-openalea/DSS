from openalea.dss import Manager
def nematodes(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Plant parasitic nematodes can cause serious damage to crop yield and crop quality. Important groups of plant parasitic nematodes are: cyst nematodes, root-knot nematodes, root-lesions nematodes, stem nematodes and free living nematodes. THE DECISION: Nematodes can best be managed by healthy crop rotations, as crops and crop varieties have a different host status for nematodes. Alternating host and non-host crops or varieties lowers infestation rates in the soil. THE MODEL: The model databases contain information about susceptibility and tolerance of 70 crops to 32 nematodes. The databases are neither soil-specific nor country-specific. PARAMETERS: The returns risks based on crops, including green manure crops, and crop rotation. This farm specific input has to be provided by the user. SOURCE: Created by H2020 project Best4Soil, based on the Dutch model www.aaltjesschema.nl, developed by Wageningen University and Research. ASSUMPTIONS: The model gives risk information, assuming that the user selected plant parasitic nematodes are present in the field.'
    '''
    
    h= Manager()
    _model= h.get_model("Best4Soil.Support.Tools", "nematodes")

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
    

