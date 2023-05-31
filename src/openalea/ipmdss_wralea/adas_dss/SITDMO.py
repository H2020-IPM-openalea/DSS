from openalea.dss import Manager
def SITDMO(weathersource, p1=1002, p2=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Orange wheat blossom midge larvae feed on developing grains, causing grains to become small and shrivelled. They can also damage the outer grain layer (pericarp), allowing water to enter. This can make the grain vulnerable to fungal infection (e.g. fusarium and septoria) and result in premature sprouting. Seed from infected crops is also associated with poor germination. Susceptible crops are at the highest risk when adult midge emergence coincides with ear emergence, particularly growth stages 53\xe2\x80\x9359. Larvae that hatch after flowering do not develop properly and cause little damage.  \n\nTHE DECISION: The model predicts the emergence of adults and associated migration of females into vulnerable crops, when increased monitoring and/or treatment may be appropriate.\nTHE MODEL: Daily temperature (degrees Celsius) and rainfall (mm) data is used to identify emergence of Orange Wheat Blossom Midge. The model runs between the months May and June, but requires weather data from the 1st of January. The model runs in three phases: Phase 1: Temperature accumulation of 250 degree days above 3 degrees from 1st January.  Phase 2 (Low risk): Lasts until mean daily temperature reaches 13 degrees Celsius, followed by rainfall (>2mm). During Phase 1 and 2, there is a low risk of emergence. Phase 3 (Medium risk): One phase 2 is complete, temperature accumulation of 160 degree days above 7 degrees. During phase 3, there is a medium risk of emergence. Upon completion of phase 3 the risk is considered high for three days and a date of emergence is predicted, which will be reported in the platform. Multiple emergence dates are possible, leading to extended periods of high risk of emergence.\nTHE PARAMETERS: The model uses daily temperature and rainfall\nREGION: This DSS was adapted from work carried out in Belgium, and is considered to be applicable, but yet to be validated in, the UK,  Luxembourg, Netherlands, France, Germany, Denmark.\nASSUMPTIONS: This DSS assumes that the crop variety use is vulnerable to damage by orange wheat blossom midge, and that the user will interpret the risk against the vulnerability of the crop growth stage on farm.\nREFERENCE: Jocquemin et al. (2014) Crop Protection 58, 6-13. https://doi.org/10.1016/j.cropro.2013.12.021 '
    '''
    
    h= Manager()
    _model= h.get_model("adas.dss", "SITDMO")

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
    

