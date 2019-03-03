# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:37:56 2019

@author: chauman.fung@kuleuven.be
"""
import numpy as np
from numpy import *
from sympy import *

# set size of the supply chain network
manufacturers=2
retailers=2
buyers=2

m = manufacturers+1 #number of manufacturers +1
r = retailers+1 #number of retailers + 1
b = buyers+1 #number of buyers +1

# define symbols   
for i in range(1,r):
    globals()['gamma'+str(i)] = symbols('gamma'+str(i))
    
for i in range(1,b):
    globals()['rho3'+str(i)] = symbols('rho3'+str(i))
   
# insert functional forms  

t1q=[]
for i in range(1,m):
    for j in range(1,r):
       t1q.append(symbols('t1q'+str(i)+str(j)))
t1q=np.reshape(t1q,(m-1,r-1))


##############################################################
## edit production cost functions here
##############################################################
f=[]
for i in range(1,m):
    f.append(Function('f'+str(i)))

f1 = (2.5*(sum([t1q[0]]))**2 +0*(sum([t1q[1]]))**2
                     + sum([t1q[0]])*sum([t1q[1]])
                     +2*(sum([t1q[0]]))+0*(sum([t1q[1]])))
f2 = (0*(sum([t1q[0]]))**2 +2.5*(sum([t1q[1]]))**2
                     + sum([t1q[0]])*sum([t1q[1]])
                     +0*(sum([t1q[0]]))+2*(sum([t1q[1]])))

#f1 = 2.5*(t1q11+t1q12)**2 + (t1q11+t1q12)*(t1q21+t1q22) + 2*(t1q11+t1q12)
#f2 = 2.5*(t1q21+t1q22)**2 + (t1q11+t1q12)*(t1q21+t1q22) + 2*(t1q21+t1q22)
f=[f1,f2]
##############################################################
t1c=[]
for i in range(1,m):
    for j in range(1,r):
       t1c.append(Function('t1c'+str(i)+str(j)))
t1c=np.reshape(t1c,(m-1,r-1))
##################################################################
## edit transaction cost faced by manufactuerers here
##################################################################
for i in range(0,m-1):
    for j in range(0,r-1):
            t1c[i,j] = 0.5*t1q[i,j]**2 +3.5*t1q[i,j]
############################################################
            
c=[]
for i in range(1,r):
    c.append(Function('c'+str(i)))
##############################################################
## edit handling cost of retailers here
############################################################
for i in range(0,r-1):
    c[i] = 0.5*(sum([t1q[:,i]]))**2
############################################################
  
d=[]
for i in range(1,b):
    d.append(Function('d'+str(i)))
##############################################################
## edit demand functions here    
############################################################
d1 = -2*rho31 - 1.5*rho32 + 1000
d2 = -2*rho32 - 1.5*rho31 + 1000
d= [d1,d2]
############################################################
t2q=[]
for i in range(1,r):
    for j in range(1,b):
       t2q.append(symbols('t2q'+str(i)+str(j)))
t2q=np.reshape(t2q,(r-1,b-1))

t2c=[]
for i in range(1,r):
    for j in range(1,b):
       t2c.append(Function('t2c'+str(i)+str(j)))
t2c=np.reshape(t2c,(r-1,b-1))
###########################################################
## edit transaction costs between retailers and consumers
#############################################################
for i in range(0,r-1):
    for j in range(0,b-1):
            t2c[i,j] = t2q[i,j] + 5
            
rho3=[]
for i in range(1,b):
    rho3.append(symbols('rho3'+str(i)))

gamma=[]
for i in range(1,r):
    gamma.append(symbols('gamma'+str(i)))

# the F function 

L1=[]
for i in range(1,m):
    for j in range(1,r):
       L1.append(Function('L1'+str(i)+str(j)))
L1=np.reshape(L1,(m-1,r-1))
for i in range(0,m-1):
    for j in range(0,r-1):
        L1[i,j] = (f[i].diff(t1q[i,j]) + t1c[i,j].diff(t1q[i,j]) 
        + c[j].diff(t1q[i,j]) - gamma[j])

L2=[]
for i in range(1,r):
    for j in range(1,b):
       L2.append(Function('L2'+str(i)+str(j)))
L2=np.reshape(L2,(r-1,b-1))
for i in range(0,r-1):
    for j in range(0,b-1):
        L2[i,j] = (t2c[i,j] + gamma[i] - rho3[j])

L3=[]
for i in range(1,r):
    L3.append(Function('L3'+str(i)))
for i in range(0,r-1):
    L3[i] = sum(t1q[:,i])-sum(t2q[i,:])

L4=[]
for i in range(1,b):
    L4.append(Function('L4'+str(i)))
for i in range(0,b-1):
    L4[i] = (sum(t2q[:,i]) - d[i])
