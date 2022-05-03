## 
# 
# Data plot function
# 
## Author: Aksel Buur Christensen
# 

import numpy as np 
from matplotlib import cm
import matplotlib.pyplot as plt 

def dataPlot(data,statistic):
    # Input: Loaded data and chosen statistic as a string: 
    # "Mean", "Variance" or "Cross-correlation"

    # Output: Plot of the chosen statistics. 
    # https://matplotlib.org/3.5.0/gallery/mplot3d/surface3d.html
    
    # Create the axis for z and y and meshgrid
    z = np.arange(np.size(data[1,:]))
    y = np.arange(np.size(data[:,1]))
    z, y = np.meshgrid(z,y)

    # Create the contourplot
    plt.contour(z,y,data,cmap=cm.coolwarm,linewidth=0)

    if statistic == "Mean":
        plt.title("Mean distribution (yz-plane)",fontsize=14,fontweight='bold') 
    
    elif statistic == "Variance":
        plt.title("Variance distribution (yz-plane)",fontsize=14,fontweight='bold')  
    
    elif statistic == "Cross correlation":
        plt.title("Cross correlation (yz-plane)",fontsize=14,fontweight='bold') 
    
    plt.show()
