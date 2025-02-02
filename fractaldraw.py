# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" 
Fractal Draw
April 2020
"""

import math
import matplotlib.pyplot as plt

def main():

    
    x = [0] 
    y = [0]

    
    #Triangles

    #Examples
    #d = [1,2,3,4,5,6] = regular hexagon
    #d = [1,3,5] or [2,4,6] = equilateral triangle

   
    #Sierpinski Carpet

    s = 10 #number of iterations

    a = [1]
    b = [3]
    c = [5]

    #piecing together the line to draw the fractal
    for i in range(1,s):
        
        if i == 1:
            a0 = a.copy()
        
        if i > 1:
            a = a0.copy()
        a.extend(b)
        a.extend(a0)
        a.extend(c)
        a.extend(a0)
        a.extend(b)
        a.extend(b)
        a.extend(c)
        a.extend(c)

        x0 = 3**(1+i)
        y0 = 2**(i)
        n = x0 - 2*y0

        a0 = a[0:n]
        b = a[n:n+y0]
        c = a[n+y0:n+2*y0]

    d = a

    for i in range(0,len(d)):
        [xnew, ynew] = trianglemove(x[i],y[i],d[i])
        x.append(xnew)
        y.append(ynew)
    
    plt.plot(x,y)
    plt.title('Sierpinski Carpet')
    plt.show()
    
    
    #Square Fractal/Snowflake 
    
    x = [0]
    y = [0]

    s = 5 #number of iterations

    z = [1,2,3,4,1,2,3,4,1]
    d = [1,4,3,2]
    d0 = []

    #piecing together the line to draw the fractal
    for k in range(1,s):
        d0 = []
        for i in range(len(d)):
            j = d[i]     
            d1 = [z[j+3],z[j+4],z[j+3],z[j+2],z[j+3]]
            #d1 = [z[j+3],z[j+4],z[j+3],z[j+2],z[j+2],z[j+3],z[j+4],z[j+3]]
            #d1 = [z[j+3],z[j+3],z[j+4],z[j+1],z[j+4],z[j+3],z[j+4],z[j+3],z[j+2],z[j+3],z[j+2],z[j+1],z[j+2],z[j+3],z[j+3]]
            d0.extend(d1)

        d = d0.copy()


    for i in range(0,len(d)):
        [xnew, ynew] = squaremove(x[i],y[i],d[i])
        x.append(xnew)
        y.append(ynew)
    
    plt.plot(x,y)
    plt.title('Another fractal')
    plt.show()



    
    #Koch Snowflake (Fractal)

    x = [0]
    y = [0]

    s = 5 #number of iterations

    z = [1,2,3,4,5,6,1,2,3,4,5,6,1]
    d = [1,5,3]
    d0 = []

    #piecing together the line to draw the fractal
    for k in range(1,s):
        d0 = []
        for i in range(len(d)):
            j = d[i]     
            d1 = [z[j+5],z[j+6],z[j+4],z[j+5]]
            #d1 = [z[j+5],z[j+6],z[j+5],z[j+3],z[j+3],z[j+5],z[j+6],z[j+5]]
            d0.extend(d1)

        d = d0.copy()
    

    for i in range(0,len(d)):
        [xnew, ynew] = trianglemove(x[i],y[i],d[i])
        x.append(xnew)
        y.append(ynew)
    
    plt.plot(x,y)
    plt.title('Koch Snowflake')
    plt.show()
    

    
    
    
    #Square Dragon Fractal Generator

    #Examples
    #d = [1,2,3,4] = square (without any repeating/iterating)
    
    x = [0]
    y = [0]

    s = 10 #number of steps of dragon fractal

    #Order 2 Sequence
    seeds = [[1,2]] #seed 1 (original dragon fractal) 
    
    #Order 3 Sequences
    #seeds = [[1,1,2],[1,1,3],[1,2,1],[1,2,2],[1,2,3],[1,2,4],[1,3,1],[1,3,2],[1,3,3],[1,3,4]]
        
    #Order 4 Sequences
    seeds = [[1,2,1,2],[1,2,2,1],[1,2,2,2],[1,2,2,3],[1,2,4,1],[1,3,3,3],[1,3,4,3],[1,3,4,4],[1,1,1,2],[1,1,2,1],[1,1,2,2],[1,1,3,1],[1,1,3,2],[1,1,3,3],[1,2,3,1]]
    
    num = 0
    
    for d in seeds:
        x = [0]
        y = [0]
        num += 1
        for k in range(0,s):
            c = []
            for i in range(0,len(d)):
                c.append(d[len(d)-1-i])
                c[i] = c[i] + 1
                if c[i] > 4:
                    c[i] = c[i] - 4
    
            d.extend(c)
            
    
        for i in range(0,len(d)):
            [xnew, ynew] = squaremove(x[i],y[i],d[i])
            x.append(xnew)
            y.append(ynew)
    
        plt.figure(num)
        plt.plot(x,y)
        plt.title('Dragon Sequence ' + str(d[0]) + str(d[1]))
        plt.show()
    
    
    
    #Triangular Tesselation Generator
    
    s = 10 #number of iterations

    #Order 2
    #seeds = [[1,3],[1,2]]

    #Best of Order 3
    #seeds = [[1,2,1],[1,1,2]]

    #Best of Order 4
    seeds = [[1,1,1,2],[1,1,1,3],[1,1,2,1],[1,1,2,3],[1,1,2,6],[1,2,1,2],[1,2,1,6],[1,2,2,1],[1,2,2,6],[1,3,2,2]]

    num = 0

    for d in seeds:
        x = [0]
        y = [0]
        num += 1
        for k in range(0,s):
            c = []
            for i in range(0,len(d)):
                c.append(d[len(d)-1-i])
                c[i] = c[i] + 2
                if c[i] > 6:
                    c[i] = c[i] - 6
    
            d.extend(c)
    
        for i in range(0,len(d)):
            [xnew, ynew] = trianglemove(x[i],y[i],d[i])
            x.append(xnew)
            y.append(ynew)
    
        plt.figure(num)
        plt.plot(x,y)
        plt.title('Tessellation Sequence ' + str(d[0]) + str(d[1]) + str(d[2]) + str(d[3]))
        plt.show()
       

def squaremove(x0,y0,d,c = 1):
    #moves the point in one of 4 directions, each 90 degrees apart

    #x0,y0 is the starting point
    #d is the direction (1 is +x axis, numbered ccw)
    #c is optional multiplier

    if d == 1:
        x = x0 + c
        y = y0

    if d == 2:
        x = x0
        y = y0 + c

    if d == 3:
        x = x0 - c
        y = y0

    if d == 4:
        x = x0 
        y = y0 - c


    return x,y

def trianglemove(x0,y0,d,c = 1):
    #moves the point in one of 6 directions, each 60 degrees apart

    #x0,y0 is the starting point
    #d is the direction (1 is +x axis, numbered ccw)
    #c is optional multiplier

    if d == 1:
        x = x0 + c
        y = y0

    if d == 2:
        x = x0 + c / 2
        y = y0 + c * math.sqrt(3) / 2

    if d == 3:
        x = x0 - c / 2
        y = y0 + c * math.sqrt(3) / 2

    if d == 4:
        x = x0 - c
        y = y0 

    if d == 5:
        x = x0 - c / 2
        y = y0 - c * math.sqrt(3) / 2

    if d == 6:
        x = x0 + c / 2
        y = y0 - c * math.sqrt(3) / 2


    return x,y



if __name__=="__main__":
    main()