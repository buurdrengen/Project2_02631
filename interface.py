# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:18:44 2022

@author: cglitz
"""

import numpy as np
# imports three-dimensional array with Nx, Ny, Nz
from loaddata import dataLoad

from input_number import inputNumber
from input_number_integers import inputNumber_int
from displayMenu import displayMenu
from statistics import dataStatistics
#from dataPlot import dataPlot
from inputFilename import inputFilename


# Define menu items
menuItems = np.array(["Load data", "Display statistics", "Generate plots", "Quit"])

# Start
while True:
    # Display menu options and ask user to choose a menu item
    choice = displayMenu(menuItems)
    # Menu item chosen
    # ------------------------------------------------------------------
    # 1. Load data
    if choice == 1:
    # Ask user to input file name and dimnensions of the array 
        # function file input 
        filename = inputFilename()
        # asks one after the other for the size of the three dimensions
        dimension_x = int(input('Please input the size of the first dimension (x-coordinate) of the 3-dimensional output array: '))
        dimension_y = int(input('Please input the size of the second dimension (y-coordinate) of the 3-dimensional output array: '))
        dimension_z = int(input('Please input the size of the third dimension (z-coordinate) of the 3-dimensional output array: '))
        # loads data. If dimensions do not fit to the dataset, an error message occurs saying so. 
        data = dataLoad(filename, dimension_x, dimension_y, dimension_z)

    # ------------------------------------------------------------------
    # 2. Display statistics
    elif choice == 2:
        try:
            data
        except:
            print('You need to load a dataset first')
            continue
        # display statistics options and shows applied filter (if a filter is active) 
        statistics_menuItems = np.array(["Mean", "Variance","Cross correlation", "Quit"])

        # Display menu options for statistics and ask user to choose a menu item
        while True:
            choice_statistics = displayMenu(statistics_menuItems)
            if choice_statistics == 4:
                break
            Yref = None 
            Zref = None
            DeltaX = None 
        #compute statistics via dataStatistics function 
<<<<<<< Updated upstream
        # test = dataStatistics(data, statistics_menuItems[choice_statistics-1])
        # print(test)
        # Remember to display y- and z-coordinates!! 
            if choice_statistics == 1:
                dataStatistics(data,"Mean")
                print('Mean temperature = {:.2f} °C'.format(dataStatistics(data, 'mean temperature')),"\n")
=======
            # returns mean of user determined y and z coordinate. Input number has to be integer, otherwise error message is displayed 
            if choice_statistics == 1:
                # mean_array = 2D array (z to y dimension) with all the means through x-dimension
                mean_array = dataStatistics(data,"Mean",Yref,Zref,DeltaX)
                z_coordinate = inputNumber_int('Please input the z_coordinate you want to display the mean for: ')
                y_coordinate = inputNumber_int('Please input the y_coordinate you want to display the mean for: ')
                # mean of input coordinates 
                mean = mean_array[z_coordinate, y_coordinate]
                print('Mean = {:.2f}'.format(mean,"\n"))
>>>>>>> Stashed changes
                continue
            # returns variance of user determined y and z coordinate. Input number has to be integer, otherwise error message is displayed 
            elif choice_statistics == 2:
<<<<<<< Updated upstream
                dataStatistics(data, "Variance")
                print('Mean growth rate = {:.2f}'.format(dataStatistics(data, 'mean growth rate')),"\n")
                continue
            elif choice_statistics ==3:
                dataStatistics(data, "Cross correlation")
                print('Standard temperature = {:.2f}'.format(dataStatistics(data, 'std temperature')),"\n")
=======
                # 2D array (z to y dimension) with all variances through x-dimesnion
                variance_array = dataStatistics(data, "Variance",Yref,Zref,DeltaX)
                z_coordinate = inputNumber_int('Please input the z_coordinate you want to display the variance for: ')
                y_coordinate = inputNumber_int('Please input the y_coordinate you want to display the variance for: ')
                # variance for input coordinates 
                variance = variance_array[z_coordinate, y_coordinate]
                print('Variance = {:.2f}'.format(variance,"\n"))
                continue
            elif choice_statistics == 3:
                Yref = inputNumber_int('Please input the y_coordinate for the cross correlation: ')
                Zref = inputNumber_int('Please input the z_coordinate for the cross correlation: ')
                DeltaX = inputNumber_int('Please input the separation in x-coordinate for which the cross-correlation shall be evaluated for: ')
                cross_correlation = dataStatistics(data, "Cross correlation", Yref, Zref, DeltaX)
                print('Cross correlation = {:.2f}'.format(cross_correlation,"\n"))
>>>>>>> Stashed changes
                continue
                           
    # ------------------------------------------------------------------
    # 4. Display plots 
    elif choice == 3: 
        # Check if the data is loaded.
        try:
            data 
        except: 
            print("You need to load a dataset first")
            continue
        # Plot the data 
        dataPlot(data)
    # 5. Quit
    elif choice == 4:
        break
    # End
    