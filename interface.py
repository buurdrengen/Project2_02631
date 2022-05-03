# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:18:44 2022

@author: cglitz
"""

import numpy as np
# imports three-dimensional array with Nx, Ny, Nz
from loaddata import dataLoad

from input_number import inputNumber
from displayMenu import displayMenu
#from statistics_2 import dataStatistics
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
        #compute statistics via dataStatistics function 
        # test = dataStatistics(data, statistics_menuItems[choice_statistics-1])
        # print(test)
            if choice_statistics == 1:
                dataStatistics(data,"Mean",Yref,Zref,DeltaX)
                print('Mean = {:.2f} °C'.format(dataStatistics(data, 'Mean',Yref,Zref,DeltaX)),"\n")
                continue
            elif choice_statistics == 2:
                dataStatistics(data, "Variance",Yref,Zref,DeltaX)
                print('Variance = {:.2f}'.format(dataStatistics(data, 'Variance',Yref,Zref,DeltaX)),"\n")
                continue
            elif choice_statistics ==3:
                dataStatistics(data, "Cross correlation",Yref,Zref,DeltaX)
                print('Cross correlation of Yref ='Yref' and Zref ='Zref' = {:.2f}'.format(dataStatistics(data, 'Cross correlation',Yref,Zref,DeltaX)),"\n")
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
    