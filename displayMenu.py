# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:01:13 2022

@author: cglitz with much inspiration from Mikkel N. Schmidt, mnsc@dtu.dk, 2015
"""
import numpy as np
from input_number import inputNumber


def displayMenu(options):
# DISPLAYMENU Displays a menu of options, ask the user to choose an item
# and returns the number of the menu item chosen.
## Usage: choice = displayMenu(options)
## Input options Menu options (array of strings)
# Output choice Chosen option (integer)
## Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    # Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
        # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice