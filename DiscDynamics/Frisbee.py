import numpy as np
# Reference:
# http://web.mit.edu/womens-ult/www/smite/frisbee_physics.pdf
# Adapted from:
# V. R. Morrison
# Physics Department, Mount Allison University, Sackville, NB Canada
class Frisbee():
    def __init__(self):
        # set initial conditions
        self.g = -9.81
        # The acceleration of gravity (m/s^2).

        self.m = 0.175
        # The mass of a standard frisbee in kilograms.

        self.RHO = 1.23
        # The density of air in kg/m^3.

        self.AREA = 0.0568
        # The area of a standard frisbee.

        self.CL0 = 0.15
        # The lift coefficient at alpha = 0.

        self.CLA = 1.4
        # The lift coefficient dependent on alpha.

        self.CD0 = 0.08
        # The drag coefficent at alpha = 0.

        self.CDA = 2.72
        # The drag coefficient dependent on alpha.
        self.ALPHA0 = -4.0

        self.cl = 0.00
        self.cd = 0.00


    def simulate(self, angle, y0,  vx0,  vy0, deltaT=0.001):
        # Calculation of the lift coefficient using the relationship given
        # by S. A. Hummel.
        self.cl = self.CL0 + (self.CLA*angle*np.pi/180.00)
        self.cd = self.CD0 + self.CDA*( ((angle-self.ALPHA0)*(np.pi/180.00))**2 )
        # Initial position x = 0.
        x = 0
        # Initial position y = y0.
        y = y0
        # Initial x velocity vx = vx0.
        vx = vx0
        # Initial y velocity vy = vy0.
        vy = vy0

        flight_path = [] # create a list 
        flight_path.append([x,y,vx,vy])
        while( y > 0.00): # while we don't hit the ground
            x,y,vx,vy =  self.step(x,y,vx,yv,deltaT) 
            # do one step and add the result to our list
            flight_path.append([x,y,vx,vy])
        return flight_path # return the list 


    def step(self,x,y,vx,vy,deltaT):
        # The change in velocity in the y direction obtained setting the            
        # net force equal to the sum of the gravitational force and the
        # lift force and solving for delta v.
        # calculatae how the velocity changes
        deltavy = ((self.RHO*(vx**2)*self.AREA*self.cl/2.0)/self.m)+self.g
        deltavy = deltavy*deltaT
        # The change in velocity in the x direction, obtained by
        # solving the force equation for delta v. (The only force
        # present is the drag force).
        deltavx = -1*self.RHO*self.AREA*self.cd*deltaT*(vx**2)
        
        # The new positions and velocities are calculated using
        # simple introductory mechanics.        
        # take the old value and add the change during our timestep
        vx = vx + deltavx
        vy = vy + deltavy
        x = x + vx*deltaT
        y = y + vy*deltaT
        return (x,y,vx,vy)
