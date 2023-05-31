def CIBSE_hourly_temperature_for_multiple_days():
    '''    b'This model calculates hourly tempertaure values based on the CIBSE model for multiple days (Chow & Levermore, 2007). The model first allocates times for when  maximum and minimum temperatures occur in each day using the CIBSE Guide A2 (1982). \nMaximum temperature is then linked, using a sinusoidal curve to the minimum temperature of the following day. Capping is introduced in this model whereby if the generated value is higher than the maximum temperature then it is reduced to the maximum tempertaure,\nand if lower than the minium temperature the generated value is changed to the minimum temperature.\n\nSOURCE: \nASSUMPTIONS: \nREFERENCE: '
    '''
    result = None; 
    # write the node code here.

    # return outputs
    return result,
