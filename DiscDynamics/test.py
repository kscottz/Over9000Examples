from Frisbee import *
import matplotlib.pyplot as plt
import numpy as np

# create a frisbee
myFrisbee = Frisbee()
angle = 10 # degrees
height = 1.0 #meters
# try different velocities in m/s 14m/s ~30mph
velocity = np.linspace(2,14,7)
#velocity = 14
for v in velocity: # for each velocity
    result = myFrisbee.simulate(angle,height,v,0) # do the sim
    result = np.array(result) # convert to numpy
    x= result[:,0] # slice out x,y values
    y= result[:,1]  
    plt.plot(x,y) # plot the values
    


plt.grid()
legends = []
for v in velocity: # create the legend names
    temp = "Velocity " + str(v) + "m/s"
    legends.append(temp)
title = "Frisbee Dynamics at Angle: " + str(angle) + " degrees" 
plt.title(title)
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.legend(legends)
plt.show()# show the plot
