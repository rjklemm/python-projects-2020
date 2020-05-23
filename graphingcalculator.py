"""
"Graphing Calculator" 
(setup for Functions, Parametric and Polar
made easy for non-Python users)

Bob Klemm
5/23/2020
"""

import numpy as np
import math
import matplotlib.pyplot as plt



#FUNCTION
# y = f(x)

#adjust window and detail here
start = -10
stop = 10
step = 0.1


x = np.arange(start,stop,step)
y = []

for i in x:

    #type function below
    y0 = math.exp(i)

    y.append(y0)
plt.plot(x,y)
plt.show()



#PARAMETRIC
# x = f(t)
# y = g(t)

#adjust window and detail here
start = 0
stop = 10
step = 0.1


t = np.arange(start,stop,step)
x = []
y = []

for i in t:

    #type functions below
    x0 = math.cos(i)
    y0 = math.sin(i)


    x.append(x0)
    y.append(y0)
plt.plot(x,y)
plt.show()



#POLAR
# r = f(t)
# theta = g(t)

#adjust window and detail here
start = 0
stop = 10
step = 0.1


t = np.arange(start,stop,step)
r = []
theta = []
x = []
y = []

for i in t:

    #type functions (r and theta) below
    r0 = math.cos(i) + 1
    theta0 = i

    r.append(r0)
    theta.append(theta0)
    x.append(r0*math.cos(theta0))
    y.append(r0*math.sin(theta0))
plt.plot(x,y)
plt.show()