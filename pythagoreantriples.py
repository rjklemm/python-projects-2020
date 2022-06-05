#Pythagorean Triples

#Bob Klemm
#10/27/2020

import math

a = range(1,25) #range maximum is for "a" and "b"

for i in a:
    for j in range(1,i):
        n = i**2 + j**2
        c = math.sqrt(n)
        if  c == math.floor(c):
            print(j,i,int(c))

#prints out pythagroean triples up to a certain value 


