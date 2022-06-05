# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:45:04 2020

@author: rjkle
"""

"""
Bob Klemm
October 31st, 2020


"""
import matplotlib.pyplot as plt

def main():
    
    #draws a shape with 90 degree angles
  
    a = [1,2]
    
    for n in range(1,16):
        b = []
        for i in reversed(a):
            j = i - 1
            if j < 1:
                j = j + 4
            b.append(j)
        for j in b:
            a.append(j)
        
    shapedraw(a)
    
def shapedraw(a):
    # a is a 1D array of directions (1-4)
    x = [0]
    y = [0] 
    
    x0 = 0
    y0 = 0
    
    for i in a:
        [x0,y0] = squaremove(x0,y0,i)
        x.append(x0)
        y.append(y0)
    
    plt.plot(x,y)
    plt.title('A Dragon')
    
def squaremove(x,y,n):
    #draws a line in a cardinal direction
        
    if n == 1:
        x = x + 1
        
    elif n == 2:
        y = y + 1
        
    elif n == 3:
        x = x - 1
         
    elif n == 4:
        y = y - 1
        
    else:
        print('not a valid input')
    
    return(x,y)
    
main()