## Input filename function
#
#
## Author: Aksel Buur Christensen
# 
# 
import os 
def inputFilename():
    # This function checks whether the file which is put in, is in the current working directory. 
    # Input: File 

    files = os.listdir(os.getcwd()) # Find all files in the current working directory. 

    while True: 
        filename = str(input('Please input a file. Remember to put .bin after the name: '))
        if filename in files:
            break
        else:
            print('The file could not be found in the current working directory!')
    return filename

#print(inputFilename())