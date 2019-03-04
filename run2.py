# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:58:39 2019

@author: chauman.fung@kuleuven.be
"""
# sol
import numpy as np
from sympy import *
from varfunc_eg3 import *
from varfunc_st import *
from starting import *
import matplotlib.pyplot as plt

datax=[]
dataq2=[]
datap2=[]
# take values from starting point
list1=compare2(list0)
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
    compare2(list1)
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
    dataq2.append(list1[0])
    datap2.append(list1[-1])
    k = k + 1 
    
print('end')
plt.scatter(datax,dataq2)
plt.show()
#plt.savefig('q1.png')
plt.scatter(datax,datap2)
#plt.savefig('p1.png')
plt.show()
