from openalea.dss import Manager
def ipmwiseDK(weathersource):
    '''    b'Dansk: Tilpas ukrudtsbek\xc3\xa6mpelsen til netop dit behov som landmand eller konsulent. Bestem selv, hvor rene dine marker skal v\xc3\xa6re - eller lad IPMwise\nguide dig, hvis du foretr\xc3\xa6kker IPM. Programmet indeholder nyttige v\xc3\xa6rkt\xc3\xb8jer, der kan hj\xc3\xa6lpe med at tilpasse indsatsen mod ukrudt til den aktuelle \nukrudtsbestand i marken og p\xc3\xa5 den m\xc3\xa5de mindske herbicidforbruget betragteligt. Programmet kan anvendes til planl\xc3\xa6gning af herbicidindsatsen p\xc3\xa5 b\xc3\xa5de\nmarkniveau og som et generelt planl\xc3\xa6gningsv\xc3\xa6rt\xc3\xb8j for planteavlskonsulenter til at finde egnede tankblandinger og tilh\xc3\xb8rende doser. Programmet\nfungerer ved hj\xc3\xa6lp af dosis-respons-data, som kommer fra effektrapporter. I Danmark arbejdes der for tiden p\xc3\xa5 ogs\xc3\xa5 at anvende programmet \ni forbindelse med kunstig intelligens, automatisk ukrudtsgenkendelse og tildelingskort.\n\nEnglish: Adapt weed management to your needs as a professional farmer or crop advisor. Decide yourself, the level of weed control \nor let the built-in IPM principles of IPMwise guide you. The program contains useful tools to adapt the effort against weeds to the \ncurrent weed population in a field and thus minimize the use of herbicides considerably. The program can be used to plan herbicide \nefforts at both field level and as a general planning tool for crop advisors to find suitable tank mixtures and corresponding dose rates. \nThe principles of the program are based on dose response data derived from efficacy reports. In Denmark, work is currently underway to \nalso use the program in conjunction with artificial intelligence, automatic weed recognition and spray maps.\n'
    '''
    
    h= Manager()
    _model= h.get_model("com.ipmwise", "ipmwiseDK")

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
    

