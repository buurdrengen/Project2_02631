## DATA LOAD FUNCTION 
# 
# Author: Aksel Buur Christensen
# 
# 
def dataLoad(filename,Nx,Ny,Nz):
    import numpy as np
    # This function takes as input: 
    # Binary file (.bin), and Nx, Ny and Nz, which are the sizes of the first, second and third dimension.
    # Here the values for Nx, Ny and Nz are specified in the filename as "32x32x8192", for Nx, Ny, Nz respectively. 
    
    # Output: data, a 3-dimensional array with size Nz x Ny x Nx

    # About the file: The .bin file represents a sequence of numbers which corresponds to indexes z,y,x. 
    # These indexes increases from 1 to Nz with y = 1 and x = 1. After the z index has gone from 1 to Nz, y gets +1. 
    # Thereafter z increases from 1 to Nz with y = 2 and x = 1. This continues until y = Ny, and then x gets +1.
    # At last z increases from 1 to Nz with y = 1 and x = 2 and z and y goes from 1 to Nz and Ny respectively. 
    # This continues until x = Nx. 
    
    # The .bin file is read with the np.fromfile, but first the file is opened. This is done with inspiration from 
    # "Python read a binary file" by Bijay Kumar: https://pythonguides.com/python-read-a-binary-file/

    with open(filename,'rb') as f: 
        init_data = np.fromfile(f,np.single) 
    # np.single is used since the data sequence is represented as floating points single precision: 
    # https://numpy.org/doc/stable/user/basics.types.html

    # Now we figure out whether the chosen Nx, Ny and Nz fits the data points in the file 
    # If it does, a three-dimensional array with dimensions Nz x Ny x Nx is returned, otherwise an error message. 

    if (np.size(init_data) == Nx * Ny * Nz):
        data = np.reshape(init_data,(Nx,Ny,Nz)).T 
        # The three-dimensional array is transposed, since the desired output as mentioned above is an Nz, Ny, Nx array. 
        # If the desired output of the three-dimensional array is Nx, Ny, Nz - the transposed sign should be removed.
        # Here it is chosen to output as Nz, Ny, Nx since it is this way the statistics will later read the data. 
        print(data)
    else: 
        print('Error: The specified dimensions do not fit with the data.')

    return data 
print(dataLoad('turbine_32x32x8192.bin',32,32,8192))