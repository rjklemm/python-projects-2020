"""
Polar Graph
Bob Klemm - 3/15/2020
"""

import math
import matplotlib.pyplot as plt


def main():
    #changeable parameters
    a = [1,0.4]
    r = [1,7]
    m = 3

    #function call
    drawpolargraph(a,r,m,1)

def drawpolargraph(a=1,r=1,m=1,n=1):

    """
    Draws the polar graph:

    Parameters:
    -----------
    *1 circle with radius 1 is default*

    a: list of radii
    1 is default
    1 is the radius of the main circle

    r: list of rotation numbers
    1 is default
    r is how many revolutions per revolution of the main circle

    *a and r go together and should be the same length*

    m: scalar
    Number of segments on the graph = 360 * m;
    m can be adjusted for fine tuning or better display

    n: scalar
    Number of revolutions for the main circle to travel.

    Displays:
    ---------
    Graph of the polar function associated with the given parameters.
    """

    x = []
    y = []

    s = 360 * m * n 
    g = s + 1
    d = math.pi / 180 #degrees to radian conversion

    for i in range(0,g):
        x0 = 0
        y0 = 0
        for j in range(0,len(a)):
            x0 = x0 + a[j]*math.cos(r[j]*i*d/m)
            y0 = y0 + a[j]*math.sin(r[j]*i*d/m)
        x.append(x0)
        y.append(y0)

    c = plt.plot(x,y)
    plt.show(c)

if __name__=="__main__":
    main()
