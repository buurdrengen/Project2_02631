# -*- coding: utf-8 -*-
"""
Spyder Editor
# Authour: C. Glitz
This is a temporary script file.
"""

import numpy as np
from loaddata import dataLoad

def dataStatistics(data,statistic,Yref=None,Zref=None,DeltaX=None):
    # Input for function:
    # data: An Nz x Ny x Nx array containing wind speed values.
    # statistic: A string specifying the statistic that should be calculated (Mean, Variance, or Cross correlation.)
    # Yref, Zref: The reference y- and z-coordinate for the cross-correlation. 
    # Only needed when statistic is Cross correlation. Denoted yref and zref below.
    # DeltaX: Separation in x-coordinate for which the cross-correlation has to be evaluated. 
    # Only needed when statistic is Cross correlation. Denoted deltax below.

    # result: A two-dimensional array with size (Ny x Nz) containing the calculated statistic for each point in the y-z plane.


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
        # Calculates the cross-correlation at the specified lag deltaX between each time series in the y-z-plane. 
        # Setting the dimension for the x-axis: 
        Nx = np.size(data,axis=2) 
        
        # Constructing the array inside the sum and making it from 0 to Nx instead from 1 to use np.sum
        # without initial-values (our experience is it messes things up). 
        c_init = data[:,:,0:Nx-DeltaX-1] * data[Zref,Yref,DeltaX:(Nx-1)]

        # Taking the sum from 0 to Nx on the x-axis: 
        array_crosscorrelation = (np.sum(c_init,axis=2)*(1/(Nx-DeltaX)))
        result = array_crosscorrelation
    
    else:
        result = "please enter a valid input for statistics"
        
    return result
# testdata=dataLoad('turbine_32x32x8192.bin',32,32,8192)
# print(dataStatistics(testdata,"Cross correlation",1,1,1))
