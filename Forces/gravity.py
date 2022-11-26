import numpy as np

def CONST_G(): # returns constant gravity with positive axis pointing away from earth's centre

    return np.array([[0,0,-9.80665]]).T

def newton_point(height=0):
    mu_earth = 398600.436e9
    r_earth = 6.371e6
    g = -mu_earth/(r_earth + height)**2

    return np.array([[0,0,g]]).T

print(CONST_G())
    