# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:15:23 2019

@author: chauman.fung@kuleuven.be
"""

import numpy as np
from sympy import *
from varfunc_eg1 import *
from varfunc_st import *
from starting import *
import matplotlib.pyplot as plt

datax=[]
dataq=[]
datap=[]

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
    datax.append(k)
    dataq.append(list1[0])
    datap.append(list1[-1])
    k = k + 1 
    
print('end')
plt.scatter(datax,dataq)
plt.show()
#plt.savefig('q2.png')
plt.scatter(datax,datap)
plt.show()
#plt.savefig('p2.png')
   
    
