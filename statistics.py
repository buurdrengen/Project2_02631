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

test_array = np.array([[[1, 2, 3, 5], [3, 4, 10, 5]], [[5, 6, 89, 5], [7, 8, 1, 5]],[[4, 3, 2, 1], [10, 9, 8, 7]]])
#print(test_array)

# Yref, Zref and DeltaX are set to None, as they are not required for mean and variance calculation
data = dataLoad('turbine_32x32x8192.bin',32,32,8192)
Yref = 1
Zref = 2
DeltaX = 2

def dataStatistics(data,statistic,Yref,Zref,DeltaX):

    if statistic == "Mean":
        # calculates the mean of the entire dataset, going through the x-dimension and return a 2D array in z/y dimension
        array_mean = np.mean(data, axis = 2)
        result = array_mean
    #in interface menu, ask for specific y and z coordinate for which the mean shall be displayed. mean = array_mean[z,y]
    
    elif statistic == "Variance":
        # calculates the variance of the entire dataset through the x dimension and returns 2D array with dimension z/y
        array_variance = np.var(data, axis = 2)
        result = array_variance
    #in interface menu, ask for specific y and z coordinate for which the mean shall be displayed. mean = array_mean[z,y]
    
    elif statistic == "Cross correlation":
        
        result = array_crosscorrelation
    
    else:
        result = "please enter a valid input for statistics"
        
    return result

print(dataStatistics(test_array, "Variance", Yref, Zref, DeltaX))

