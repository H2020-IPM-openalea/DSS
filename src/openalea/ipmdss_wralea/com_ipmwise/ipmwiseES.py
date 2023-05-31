from openalea.dss import Manager
def ipmwiseES(weathersource):
    '''    b'Adapta tu manejo de malas hierbas a tus necesidades como un agricultor profesional o un asesor de cultivos. \nDecide por ti mismo el nivel de control de malas hierbas o utiliza el modulo basado en IPM del IPMwise para guiarte. \nCaracteristicas principales: Las herramientas integradas en IPMWise pueden asistirte en planificar y decidir \nlas mejores estrategias de control de malas hierbas en tus fincas. Puedes simular como afectan las diferentes\ncondiciones de la parcela a la necesidad de control y a las herramientas disponibles. En caso de que no tengas \nrecomendaciones especificas para controlar tus malas hierbas en un momento determinado, IPMWise te permite \nsimular si en momentos anteriores o posteriores al actual es posible controlar tus infestaciones de malas hierbas.  \n'
    '''
    
    h= Manager()
    _model= h.get_model("com.ipmwise", "ipmwiseES")

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
    

