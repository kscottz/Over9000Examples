from Frisbee import *
import matplotlib.pyplot as plt
import numpy as np

myFrisbee = Frisbee()
angle = 20
height = 0.5
velocity = np.linspace(2,14,7)
for v in velocity:
    result = myFrisbee.simulate(angle,height,v,0)
    result = np.array(result)
    x= result[:,0]
    y= result[:,1]
    plt.plot(x,y)
    


plt.grid()
legends = []
for v in velocity:
    temp = "Velocity " + str(v) + "m/s"
    legends.append(temp)
title = "Frisbee Dynamics at Angle: " + str(angle) + " degrees" 
plt.title(title)
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.legend(legends)
plt.show()
