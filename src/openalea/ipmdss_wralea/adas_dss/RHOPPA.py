def RHOPPA(p1=1001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b'THE PEST: Aphids can transmit barley/cereal yellow dwarf viruses (BYDV). Initially, aphids colonise relatively few crop plants. However, the second-generation tends to move away from the plant originally colonised. Controlling this generation is a key part of a BYDV management strategy.\n\nTHE DECISION: This DSS indicates the best time to monitor crops for aphids. If infestations are high, and non-chemical control options are unlikely to prevent second generation emergence, treatment should be considered to limit the spread of the virus.\nTHE MODEL: The second generation is likely to be present when the accumulated daily air temperatures, above a baseline temperature of 3\xc2\xbaC, reaches T-Sum 170. \nTHE PARAMETERS: The model uses Date of last spray application, daily temperature\nREGION: This DSS was adapted from work carried out in the UK, and is considered applicable, but not yet validated in, Belgium, Luxembourg, Netherlands, France, Germany, Rep. Ireland, and Denmark.\nASSUMPTIONS: This DSS assumes that the user will update the date of last insecticide applications. Its also assumes that no aphids found or insecticide treatment applied at 170DD, and restarts calculations. 2nd generation development time is consistent across regions.  \nREFERENCE: UK Agricultural and Horticultural Development Board (2022). https://ahdb.org.uk/bydv '
    '''
    result = None; 
    # write the node code here.
    
    # return outputs
    return result,
