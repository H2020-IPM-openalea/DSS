from openalea.dss import Manager
def LeafRustGeneticGroupFrequency(weathersource, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'RustWatch is an established stakeholder driven early-warning system to improve preparedness  and resilience to emerging rust diseases on wheat. Rust diseases are very dynamic, which makes  it very important to follow changes in aggressiveness and spreading pattern, e.g. the existing  population of wheat yellow rust has been replaced by invasive races of non-European origin (2011)  and since 2016 Europe has experienced more severe epidemics of wheat stem rust. If you want more  detailed information about the collected rust data, take a look at the GRRC platform.  https://gis-au.maps.arcgis.com/apps/dashboards/6817a33478df49d39176863fdc67fe15\nRustWatch partners keep an eye on the development of rust species and races in order to evaluate  their potential impact on agricultural productivity. and finally develop research and communication  infrastructures including stakeholder networks.. The research and phenotyping is essential for the  plant breeders screening for new resistant cultivars.\nRustWatch engages 12 universities/research institutes, 5 agricultural advisory services, and 7  SMEs/industries. After the project ended in 2022, RustWatch is now a \xe2\x80\x9cRustWatch - a wheat rust  network for Europe\xe2\x80\x9d. Pan-European surveillance, race phenotyping and other research activities will  continue based on coordination of related projects, national activities and agreed business models.  Everybody interested in early warning and wheat rust diseases are welcome to join this network and  participate in RustWatch activities.'
    '''
    
    h= Manager()
    _model= h.get_model("dk.au.agro", "LeafRustGeneticGroupFrequency")

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
    

