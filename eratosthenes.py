# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:49:45 2018

@author: Bob
"""

import math

def main():
    
    primes = sieve(200)
    print(primes)
    
    
def sieve(n):
    
    """Find primes less than or equal to n
    
    Inputs
    ------
    n : an integer
    
    Returns
    -------
    primes : list of primes
    """
    
    primes = []
    a = 2
    while a <= n:
        b = prime(a)
        if b is True:
             primes.append(a)       
        a = a + 1
    
    return primes
    

def prime(n):
    
    
    """Finds if a number is prime
     
    Inputs
    ------
    n : an integer
    
    Returns
    -------
    b : Boolean (TRUE if prime)
    """
    m = math.floor((n)**.5)
    k = 1
    b = True
    
    if n == 1:
        b = False
        return
    
    else:
        while k <= m:
            a = n/k
            a2 = math.floor(a)
            if a == a2 and a != 1 and a != n:
                b = False
                break
            k = k + 1
    
    return b
    
    
    
if __name__=="__main__":
    main()