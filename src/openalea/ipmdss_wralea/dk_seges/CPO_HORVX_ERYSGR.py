def CPO_HORVX_ERYSGR(p1=2001, timestart='2022-03-01', timeend='2022-08-01'):
    '''    b"THE PEST: powdery mildew (Blumeria graminis) can attack barley. \nTHE DECISION: Fungicide treatments may need to be applied between early tillering (GS 26)  and full flowering (GS 65), to protect leaves from powdery mildew and yield losses. \nTHE MODEL: The CPO powdery mildew model is recommending treatments in barley when thresholds are exceeded.  The risk of attack is based on visual monitoring using frequency of plants attacked.  The disease observation is the percentage of plants showing any infection.  For example, if 25 plants out of 100 show even a very small amount of disease and the remaining 75 plants are completely healthy, then the observation is 25%. In susceptible cultivars treatments are recommended at lower incidence levels than in resistant cultivars.  If a green color appears then no action is needed, yellow means that a limited risk is recognized, while red indicates that action is recommended.  If treatments are recommended, specific fungicides known to be effective against this disease should be chosen.  When running the powdery mildew model, the risk for yield losses from other diseases is not considered. If no action is recommended it is advised to revisit the crop after about one week to make a new evaluation of the risk. \n  \nTHE PARAMETERS  To obtain accurate risk  predictions it is essential to click on the 'Edit parameters' button to enter information on the cultivar's susceptibility to powdery mildew. Only two categorizes are used susceptible and resistant, if a cultivar is categorized as partly resistant,  it is recommended to considered it as susceptible.  Enter the specific growth stages at the time when the crop monitoring was done.  Enter information on the incidence of attacked plants by powdery mildew based on scouting the crop. Between GS  29-31 whole crop should be assessed. Between GS 32 and 40 assessments should only be done on 3 upper leaves.  Entering information on last fungicide spray dates is vital for the model. This is also done in 'Edit parameters'.  Clicking on 'Save' will keep the information entered and the model will immediately update the risk estimate.  After spraying, the model assumes that the crop is protected for  14 days if a broad spectrum fungicide has been applied.\n     \nSOURCE: Created by Aarhus University and SEGES and released in Denmark in 2000. The whole CPO model has been tested in the Nordic and Baltic countries previously, but this might not have included testing of the specific mildew part.  This model may be of use in other countries in Northern Europe."
    '''
    result = None; 
    # write the node code here.
    
    # return outputs
    return result,
