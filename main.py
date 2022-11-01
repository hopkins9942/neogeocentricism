
# Ephemerides:
# https://docs.astropy.org/en/stable/coordinates/solarsystem.html

# Frames:
# ICRS is centred on barycentre of solar system (bad)
# GCRS is geocentric (good)


import numpy as np

import matplotlib.pyplot as plt

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import GCRS, get_body

frame = GCRS()



def xyz(eph):
    """takes SkyCoord object in GCRS frame and coverts into x, y and z coords
    in geocentric ecliptic frame
    coord system has positive x axis along ra=0, dec=0, positive y in ecliptic plane
    """
    assert isinstance(eph.frame, GCRS)
    
    obl = 23.4*np.pi/180 # Earth axial tilt relative to ecliptic
    
    dist = eph.distance
    ra = eph.ra
    dec = eph.dec
    
    x = dist*np.cos(dec)*np.cos(ra)
    y = dist*(np.cos(obl)*np.cos(dec)*np.sin(ra) + np.sin(obl)*np.sin(dec))
    z = dist*(np.cos(obl)*np.sin(dec) - np.sin(obl)*np.cos(dec)*np.sin(ra))
    
    return(x,y,z)




tStart = Time('2010-03-20')
tEnd = tStart + 10*u.yr
t = np.linspace(tStart, tEnd, 200)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
bodies = ['moon', 'sun', 'mercury', 'venus', 'mars', 'jupiter', 'saturn']
for b in bodies:
    eph = get_body(b, t)
    x,y,z = xyz(eph)
    ax1.plot(x, y, label=b)
    ax2.plot(z, label=b)
ax1.set_aspect('equal')
ax1.legend()
ax2.legend()





class Model:
    """Contains model, outputs chi2 value, can be inputted to fit"""
    def __init__(self):
        pass
        
        
        
        
class Cycle:
    def __init__(self):
        pass
        