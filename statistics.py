# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#Input for function:
# data: An Nz x Ny x Nx array containing wind speed values.
#statistic: A string specifying the statistic that should be calculated (Mean, Variance, or Cross correlation.)
#Yref, Zref: The reference y- and z-coordinate for the cross-correlation. Only needed when statistic is Cross correlation. Denoted yref and zref below.
#DeltaX: Separation in x-coordinate for which the cross-correlation has to be evaluated. Only needed when statistic is Cross correlation. Denoted deltax below.

# result: A two-dimensional array with size (Ny x Nz) containing the calculated statistic for each point in the y-z plane.

import numpy as np
from loaddata import dataLoad
data = dataLoad('turbine_32x32x8192.bin',32,32,8192)

if statistic == "Mean":
    result = 
    
elif statistic == "Variance":
    
elif statistic == "Cross correlation":
    
else:
    result = "please enter a valid input for statistics"



#def dataStatistics(data, statistic, Yref, Zref, DeltaX):
# Insert your code here
#return result


