# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:15:23 2019

@author: chauman.fung@kuleuven.be
"""

#to clear: %reset

#import itertools
import numpy as np
from sympy import *
from varfunc_def4 import *
from varfunc_st import *
from starting import *


# take values from starting point
list1=compare3(list0)
print(list1)

# start iterations
print('number of iterations=',1) 
for i in range(0,len(L)):    
    if Abs(list1[i]-list0[i]) <= epsilon:
        print(str(list0[i]),str(list1[i])+': diff < epsilon')
    else: 
        print(str(list0[i]),str(list1[i])+': diff > epsilon, continue')

k=2

for k in range(k,maxiter):
    print('number of iterations=',k)    
    x=list(list1)
    compare3(list1)
    if sum(bool(Abs(list1[i]-x[i]) < epsilon) for i in range(0,len(L)))<len(L):
        for i in range(0,len(L)):       
            if Abs(list1[i]-x[i]) <= epsilon:
                print(str(list1[i]),str(x[i])+': diff<epsilon ')
            else: 
                print(str(list1[i]),str(x[i])+': diff>epsilon, continue ')
    else:
        print('Solution ='+str(list1))
        print('end with iterations ='+ str(k))
        break
    k = k + 1 
print('end')    
    
