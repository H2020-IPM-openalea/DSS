from openalea.dss import Manager
def ipmwiseNO(weathersource):
    '''    b'VIPS-Ugras 2.0 er en ny versjon av VIPS-ugras. IPM Consult har utviklet systemet og som p\xc3\xa5 dansk heter IPMwise. \nDet er tilpasset norske forhold av Norsk institutt for bio\xc3\xb8konomi (NIBIO) i samarbeid med Norsk Landbruksr\xc3\xa5dgiving (NLR). \nDet er nye beregninger og tilpasninger, men det er mye det samme innholdet som gamle VIPS-Ugras. VIPS-Ugras 2.0 krever \ninnlogging. Fordelen med innlogging er at systemet kan huske skiftene dine. Systemet er gratis i Norge. Du kan velge \xc3\xa5 \nbruke ferdig innlagte effektkrav eller velge dine egne effektkrav. For en optimal plantevernl\xc3\xb8sning for de fleste forhold \nanbefaler vi at du bruker systemets effektkrav  \n'
    '''
    
    h= Manager()
    _model= h.get_model("com.ipmwise", "ipmwiseNO")

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
    

