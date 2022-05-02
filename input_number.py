# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:23:14 2022

@author: cglitz with much inspiration from Mikkel N. Schmidt, mnsc@dtu.dk, 2015
"""

def inputNumber(prompt):
# INPUTNUMBER Prompts user to input a number
## Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
# number. Repeats until user inputs a valid number.
##
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num
    
