
# Ephemerides:
# https://docs.astropy.org/en/stable/coordinates/solarsystem.html

# Frames:
# ICRS is centred on barycentre of solar system (bad)
# GCRS is geocentric (good)


import numpy as np

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import GCRS, get_body

frame = GCRS()

# ephemerides example use:
tStart = Time('2014-12-25')
tEnd = tStart + 1*u.yr
t = np.linspace(tStart, tEnd)
print(t)
eph = get_body('moon', t)
# returns array-like object with ra, dec and distance at each time
print(eph)
print(eph.ra, eph.dec)


class Model:
    """Contains model, outputs chi2 value, can be inputted to fit"""
    def __init__(self):
        pass
        
        
        
        
class Cycle:
    def __init__(self):
        pass
        