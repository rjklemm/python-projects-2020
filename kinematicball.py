"""
2D Kinematics of a Bouncing Ball (Simple Simulation)

Bob Klemm - 3/12/2020

"""
import math
import matplotlib.pyplot as plt

def main():

    ballkinematics(1,[2.5,1],0.8,10,0.01)
    return 0


def ballkinematics(h,v,c,tf,dt):

    """ This function calculates and displays a graph of height vs horizontal distance 
    for a bouncing ball given five parameters.

    Parameters:
    -----------
    h: scalar (h >= 0)
    initial height (meters)

    v: vector (v0, theta)
    v0 is the magnitude of the initial velocity vector
    theta is between -pi/2 and pi/2 radians
    initial velocity (meters/sec)

    c: scalar (0 < c <= 1)
    ratio of bounce height of peak n+1 to bounce height of peak n
    bounce coefficient (unitless constant)

    tf: scalar (t > 0)
    how many seconds the graph will show, total change in time

    dt: scalar (dt < t)
    the timestep between measurements for the simulation
    I recommend keeping this below 0.1 for a better approximation.

    Returns:
    --------
    1. 3-column array of (t,x,y) values

    2. Graph of y vs. x

    """

    xc = 0 #curent x
    x = [0] #initial horizontal distance
    yc = h #current y
    y = [h] #initial height

    v0 = v[0]
    theta = v[1]
    vx = v0 * math.cos(theta) #initial horizontal velocity
    vy = v0 * math.sin(theta) #initial vertical velocity
    g = -9.8 #graviational constant (meters/sec/sec)

    tc = 0 #current simulation time
    t = [tc];

    while tc < tf:
        #kinematics equations
        xc = xc + dt*vx 
        yc = yc + dt*vy + .5*g*dt**2
        #vx does not change
        vy = vy + g * dt 
        tc = tc + dt

        if yc < 0: #rough simulation of the bounce 
            yc = abs(yc)
            vy = abs(vy*c)

        t.append(tc)
        x.append(xc)
        y.append(yc)
    
    a = plt.plot(x,y)
    plt.show(a)

    return [t,x,y]
    

if __name__=="__main__":
    main()