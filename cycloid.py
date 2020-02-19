# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:44:48 2019

@author: Bob
"""

import numpy as np
import matplotlib.pyplot as plt
import Render as rndr
import Animate as ani
import Model as md


def main():
    
    t = np.arange(0,4*np.pi,np.pi/20)
    x1 = t - np.sin(t)
    x2 = x1 + np.pi
    y = 1 - np.cos(t)
    
    plt.plot(x1,y,'r')
    plt.plot(x2,y,'b')
    
    
if __name__=="__main__":
    main()