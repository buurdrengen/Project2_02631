# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:18:44 2022

@author: cglitz
"""
# Import functions
import numpy as np
from loaddata import dataLoad
from input_number import inputNumber
from input_number_integers import inputNumber_int
from displayMenu import displayMenu
from statistics import dataStatistics
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
    # Ask user to input file name and dimensions of the array 
        # function file input 
        filename = inputFilename()
        # asks one after the other for the size of the three dimensions
        dimension_x = int(inputNumber('Please input the size of the first dimension (x-coordinate) of the 3-dimensional output array: '))
        dimension_y = int(inputNumber('Please input the size of the second dimension (y-coordinate) of the 3-dimensional output array: '))
        dimension_z = int(inputNumber('Please input the size of the third dimension (z-coordinate) of the 3-dimensional output array: '))
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
        # Returns mean of the data, but only showing the chosen y- and z-coordinates by the user. 
        # Input number has to be integer, otherwise error message is displayed. 

        # The dataStatistics takes an Nz x Ny x Nx array and calculates the desired statistics from it. 
        # Remember this means Nz is the first dimension, Ny is the second dimension and Nx is the 

            if choice_statistics == 1:
                # mean_array = 2D array (z to y dimension) with all the means through x-dimension
                mean_array = dataStatistics(data,"Mean",Yref,Zref,DeltaX)
               
                # asks user for z and y coordinate they want to calculate the mean for. Displays error and asks again for valid coordinate if input number higher than input array 
                # more elegant would be: write function which asks for z and y coordinate and is called for all 3 statistics
                # if proven to work, can be copied to Variance and Correlation option 
                while(True):
                    z_coordinate = inputNumber_int('Please input the z_coordinate (0-index,integer) you want to display the mean for\n(Remember Nz is the first dimension, Ny the second and Nx the third): ') 
                    # exits while loop and continues if input coordinate is valid because it is lower than the z dimension of the input data
                    if 0 <= z_coordinate < dimension_z:
                        break
                    #if user input is bigger than original data, error message is displayed and the user is asked again to input a valid z-coordinate
                    else: 
                        print("The value for the z-coordinate must be positive and lower than the size of the array's first dimension")
               # same as for z for the y-coordinate. 
                while True:
                    y_coordinate = inputNumber_int('Please input the y_coordinate (0-index, integer) you want to display the mean for: ')
                    if 0 <= y_coordinate < dimension_y:
                        break
                    else: 
                        print("The value for the y-coordinate must be positive and lower than the size of the array's second's dimension")
                # Mean of input coordinates 
                # Remember 0-index. 
                mean = mean_array[z_coordinate, y_coordinate]
                print('Mean = {:.4f}'.format(mean,"\n"))
                print('')
                continue
               
            # Returns variance of user determined y and z coordinate. 
            # Input number has to be integer, otherwise error message is displayed 
            elif choice_statistics == 2: 
                # 2D array (z to y dimension) with all variances through x-dimesnion
                variance_array = dataStatistics(data, "Variance",Yref,Zref,DeltaX)

                # Copy lines from mean calculation to ask for y and z coordinates 
                while(True):
                    z_coordinate = inputNumber_int('Please input the z_coordinate (0-index, integer) you want to display the variance for\n(Remember Nz is the first dimension, Ny the second and Nx the third): ') 
                    # exits while loop and continues if input coordinate is valid because it is lower than the z dimension of the input data
                    if 0 <= z_coordinate < dimension_z:
                        break
                    #if user input is bigger than original data, error message is displayed and the user is asked again to input a valid z-coordinate
                    else: 
                        print("The value for the z-coordinate must be positive and lower than the size of the array's first dimension")
               # same as for z for the y-coordinate. 
                while True:
                    y_coordinate = inputNumber_int('Please input the y_coordinate you want to display the variance for: ')
                    if 0 <= y_coordinate < dimension_y:
                        break
                    else: 
                        print("The value for the y-coordinate must be positive and lower than the size of the array's second's dimension")

                # Variance for input-coordinates 
                variance = variance_array[z_coordinate, y_coordinate]
                print('Variance = {:.4f}'.format(variance,"\n"))
                print("")
                continue
            
            elif choice_statistics == 3:
                # Cross correlation, choose Zref, Yref and DeltaX 

                while(True):
                    Zref = inputNumber_int('Please input the reference z-coordinate (Zref (0-index, integer)) for the cross correlation\n(Remember Nz is the first dimension, Ny the second and Nx the third): ') 
                    # Exits while loop and continues if input coordinate is valid because it is lower than the z dimension of the input data
                    if 0 <= Zref < dimension_z:
                        break
                    # If user input is bigger than original data, error message is displayed and the user is asked again to input a valid z-coordinate
                    else: 
                        print("The value for the z-coordinate must be positive and lower than the size of the array's first dimension")
               # Same as for z for the y-coordinate. 
                while True:
                    Yref = inputNumber_int('Please input the reference y-coordinate (Yref (0-index, integer)) for the cross correlation: ')
                    if 0 <= Yref < dimension_y:
                        break
                    else: 
                        print("The value for the y-coordinate must be positive and lower than the size of the array's second dimension") 
                while True: 
                    DeltaX = inputNumber_int('Please input the separation in x (lags, integer) the cross correlation shall be evaluated for\n(Remember Nz is the first dimension, Ny the second and Nx the third): ')
                    # Has to be DeltaX <= dimension_x - 1 or DeltaX < than dimension_x when taking the lags. 
                    if 0 < DeltaX < dimension_x:
                        break
                    else: 
                        print("The value for DeltaX must be positive and lower than the size of the data's third dimension") 
                    # Remember 0-index
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
            # Using the same while-loop to make sure the user input valid coordinates.

            while(True):
                Zref = inputNumber_int('Please input the reference z-coordinate (Zref) for the cross correlation\n(Remember Nz is the first dimension, Ny the second and Nx the third): ') 
                # Exits while loop and continues if input coordinate is valid because it is lower than the z dimension of the input data
                if 0 <= Zref < dimension_z:
                    break
                # If user input is bigger than original data, error message is displayed and the user is asked again to input a valid z-coordinate
                else: 
                    print("The value for the z-coordinate must be positive and lower than the size of the array's first dimension")
               # Same as for z for the y-coordinate. 

            while True:
                Yref = inputNumber_int('Please input the reference y-coordinate (Yref) for the cross correlation: ')
                if 0 <= Yref < dimension_y:
                    break
                else: 
                    print("The value for the y-coordinate must be positive and lower than the size of the array's second dimension")

            while True: 
                DeltaX = inputNumber_int('Please input the separation in x (lags) the cross correlation shall be evaluated for\n(Remember Nz is the first dimension, Ny the second and Nx the third): ')
                if 0 < DeltaX < dimension_x:
                    break
                else: 
                    print("The value for DeltaX must be positive and lower than the size of the data's third dimension") 
            
            # Then the plot is created 
            data_crosscorrelation = dataStatistics(data,"Cross correlation",Yref-1,Zref-1,DeltaX)
            dataPlot(data_crosscorrelation,"Cross correlation")
        
        elif choice_plot == 4: 
            break


    # 5. Quit
    elif choice == 4:
        break
    # End
    