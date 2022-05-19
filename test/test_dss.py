# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:57:47 2013

@author: lepse
"""

from alinea.astk.Weather import sample_weather
from openalea.dss.datamanipulation import contamination_risk
from pandas import date_range

def test_fake_dss():
    seq, weather=sample_weather()
    risk = contamination_risk(weather, seq)
    assert risk == 0
    seq = date_range('2000-10-01', '2000-10-05', freq='H', tz='utc')
    risk = contamination_risk(weather, seq)
    assert risk == 46
