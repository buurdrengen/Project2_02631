# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:18:44 2022

@author: cglitz
"""
# Import
import numpy as np
from loaddata import dataLoad
from input_number import inputNumber
from input_number_integers import inputNumber_int
from displayMenu import displayMenu
from statistics_2 import dataStatistics
from dataPlot import dataPlot
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
            print('You need to load a dataset first, please try again.')
            continue

        # Display statistics options
        statistics_menuItems = np.array(["Mean", "Variance","Cross correlation", "Quit statistics"])

        # Display menu options for statistics and ask user to choose a menu item
        while True:
            choice_statistics = displayMenu(statistics_menuItems)
            if choice_statistics == 4:
                break
            Yref = None
            Zref = None
            DeltaX = None
        # Compute statistics via dataStatistics function 
        # Remember to display y- and z-coordinates!! 
            # Returns mean of the data, but only showing the chosen y- and z-coordinates by the user. 
            # Input number has to be integer, otherwise error message is displayed. 

            if choice_statistics == 1:
                # mean_array = 2D array (z to y dimension) with all the means through x-dimension
                mean_array = dataStatistics(data,"Mean",Yref,Zref,DeltaX)
               
                # asks user for z and y coordinate they want to calculate the mean for. Displays error and asks again for valid coordinate if input number higher than input array 
                # more elegant would be: write function which asks for z and y coordinate and is called for all 3 statistics
                # if proven to work, can be copied to Variance and Correlation option 
                while(True):
                    z_coordinate = inputNumber_int('Please input the z_coordinate you want to display the mean for: ') 
                    # exits while loop and continues if input coordinate is valid because it is lower than the z dimension of the input data
                    if z_coordinate <= dimension_z:
                        break
                    #if user input is bigger than original data, error message is displayed and the user is asked again to input a valid z-coordinate
                    else: 
                        print("The value for the z-coordinate must be lower than the size of the array's third dimension")
               # same as for z for the y-coordinate. 
                while True:
                    y_coordinate = inputNumber_int('Please input the y_coordinate you want to display the mean for: ')
                    if y_coordinate <= dimension_y:
                        break
                    else: 
                        print("The value for the y-coordinate must be lower than the size of the array's second's dimension")
                # Mean of input coordinates 
                # -1 because index starts with 0 whereas input coordinate is always one more. e.g. Input : 10 is index 9. 
                mean = mean_array[z_coordinate-1, y_coordinate-1]
                print('Mean = {:.2f}'.format(mean,"\n"))
                print('')
                continue
               
            # Returns variance of user determined y and z coordinate. Input number has to be integer, otherwise error message is displayed 
            elif choice_statistics == 2: 
                # 2D array (z to y dimension) with all variances through x-dimesnion
                variance_array = dataStatistics(data, "Variance",Yref,Zref,DeltaX)
                # copy lines from mean calculation to ask for y and z coordinates 
                
                z_coordinate = inputNumber_int('Please input the z_coordinate you want to display the variance for: ')
                y_coordinate = inputNumber_int('Please input the y_coordinate you want to display the variance for: ')
                # variance for input coordinates 
                variance = variance_array[z_coordinate, y_coordinate]
                print('Variance = {:.2f}'.format(variance,"\n"))
                print("")
                continue
            
            elif choice_statistics == 3:
                #copy lines from above but here with Yref and Zref. What is limit for DeltaX? Also maximal size of x-coordinate? 
                Yref = inputNumber_int('Please input the reference y_coordinate (Yref) for the cross correlation: ')
                Zref = inputNumber_int('Please input the reference z_coordinate (Zref) for the cross correlation: ')
                DeltaX = inputNumber_int('Please input the separation in x-coordinate (lags) for which the cross-correlation shall be evaluated for: ')
                cross_correlation = dataStatistics(data, "Cross correlation", Yref, Zref, DeltaX)
                print(cross_correlation)
                print('')
                continue
                           
    # ------------------------------------------------------------------
    # 4. Display plots 
    elif choice == 3: 
        # Check if the data is loaded.
        try:
            data 
        except: 
            print("You need to load a dataset first, please go back and try again.")
            continue

        # Menu for choosing which statistic to plot.
        plot_menuitems = np.array(["Mean", "Variance","Cross correlation","Quit plots"])

        choice_plot = displayMenu(plot_menuitems)

        # Plotting the different choices: 
        if choice_plot == 1: 
            data_mean = dataStatistics(data,"Mean")
            dataPlot(data_mean,"Mean")
        
        elif choice_plot == 2:
            data_variance = dataStatistics(data,"Variance")
            dataPlot(data_variance,"Variance")
        
        elif choice_plot == 3:
            # First the user has to input the reference y- and z-coordinate and moreover the DeltaX (the lags).
            # Then the plot is created 
            Yref = int(inputNumber_int('Please input the reference y_coordinate (Yref) for the cross correlation:'))
            Zref = int(inputNumber_int('Please input the reference z_coordinate (Zref) for the cross correlation:'))
            DeltaX = int(inputNumber_int('Please input the separation in x-coordinate (lags) for which the cross-correlation shall be evaluated for:'))
            data_crosscorrelation = dataStatistics(data,"Cross correlation",Yref,Zref,DeltaX)
            dataPlot(data_crosscorrelation,"Cross correlation")
        
        elif choice_plot == 4: 
            break


    # 5. Quit
    elif choice == 4:
        break
    # End
    