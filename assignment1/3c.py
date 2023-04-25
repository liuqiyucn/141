import numpy as np
import matplotlib.pyplot as plt
import os
import sympy
from pylab import *
import matplotlib.animation as animation
from IPython import display
import math

# analytic expression
def analytic(epsilon, a, theta):
    theta = math.radians(theta) # convert to radian
    radius = a*(1-epsilon**2)/(1+epsilon*np.cos(theta))
    return radius*np.cos(theta),radius*np.cos(theta)

earth_x = []
earth_y = []
# earth 
for i in range(360):
    x,y = analytic(0.01671, 1, i)
    earth_x.append(x)
    earth_y.append(y)

mars_x = []
mars_y = []
# earth 
for i in range(360):
    x,y = analytic(0.093, 1.5273, i)
    mars_x.append(x)
    mars_y.append(y)

x_plot = []
y_plot = []

figure(1)
# animation
for i in range(len(earth_x)):

    x_plot.append(earth_x[i])
    y_plot.append(earth_y[i])
     
    # Plotting graph
    plt.plot(x_plot, y_plot, color = 'green')
    plt.pause(0.01)

plt.show()

figure(2)

x_plot = x_plot.clear()
y_plot = y_plot.clear()
x_plot = []
y_plot = []

#animation
for i in range(len(mars_x)):

    x_plot.append(mars_x[i])
    y_plot.append(mars_y[i])
 
    # Mention x and y limits to define their range
    plt.xlim(-5,25)
    plt.ylim(-5,5)

     
    # Plotting graph
    plt.plot(x_plot, y_plot, color = 'red')
    plt.pause(0.01)

plt.show()