## 
# 
# Data plot function
# 
## Author: Aksel Buur Christensen
# 

import numpy as np 
from matplotlib import cm
import matplotlib.pyplot as plt 
from statistics import *
from loaddata import dataLoad
from statistics import dataStatistics
testdata = dataLoad('turbine_32x32x8192.bin',32,32,8192)
datamean = dataStatistics(testdata,'Mean')
datavar = dataStatistics(testdata,'Variance')
datacross = dataStatistics(testdata,'Cross correlation',1,1,1)
def dataPlot(data,statistic):
    # Input: Loaded data and chosen statistic as a string: 
    # "Mean", "Variance" or "Cross-correlation". 

    # Output: Plot of the chosen statistics. 
    # https://matplotlib.org/3.5.0/gallery/mplot3d/surface3d.html
    
    # Create the axis for z and y and meshgrid
    z = np.arange(np.size(data[1,:]))
    y = np.arange(np.size(data[:,1]))
    z, y = np.meshgrid(z,y)

    # Axis-titles - remember x-axis is y and y-axis is z! 
    plt.xlabel('y-axis')
    plt.ylabel('z-axis')

    # Create the contourplot
    plt.contour(z,y,data,cmap=cm.coolwarm,linewidth=0)

    
    # Create titles that changes from the input: 
    if statistic == "Mean":
        plt.title("Mean distribution (yz-plane)",fontsize=14,fontweight='bold') 
    
    elif statistic == "Variance":
        plt.title("Variance distribution (yz-plane)",fontsize=14,fontweight='bold')  
    
    elif statistic == "Cross correlation":
        plt.title("Cross correlation (yz-plane)",fontsize=14,fontweight='bold') 
    
    cmap = plt.get_cmap('coolwarm')
    sm = plt.cm.ScalarMappable(cmap=cmap)
    plt.colorbar(sm)
    plt.show()

print(dataPlot(datacross,'Cross correlation'))