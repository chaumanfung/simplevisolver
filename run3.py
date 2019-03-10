# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:22:28 2019

@author: chauman.fung@kuleuven.be
"""
import numpy as np
from sympy import Abs
import matplotlib.pyplot as plt
import timeit #use timer
start_time = timeit.default_timer()

from def_class8 import *
from starting import *

datax=[]
dataq=[]
datap=[]

# take values from starting point
list1=compare3(list0)

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
plt.scatter(datax,datap)
plt.show()

# show time elapsed
elapsed = timeit.default_timer() - start_time
print('elasped time='+str(elapsed)+'s')

#########################################################################
# reporting results #
#########################################################################

# match solutions to variable list
solmatch = {orglist[i]: oplist[i] for i in range(0,len(L))}

# report prices 
pm = []
pm=creasym(pm,'pm',mlist,rlist)
for i in range(0,len(mlist)):
    for j in range(0,len(rlist)):
        pm[i,j]=f[i].diff(t1q[i,j])+ t1c[i,j].diff(t1q[i,j])
        pm[i,j]=pm[i,j].subs(solmatch)
print('prices facing manufacturers ='+str(pm))
pr = []
pr=creasym2(pr,'pr',rlist)
for i in range(0,len(rlist)):
    pr[i]=solmatch[gamma[i]]
print('prices facing retailers ='+str(pr))
pb = []
pb=creasym2(pb,'pb',blist)
for i in range(0,len(blist)):
    pb[i]=solmatch[rho3[i]]
print('prices facing markets ='+str(pb))

# report demand
t1d = []
t1d=creasym(t1d,'t1d',mlist,rlist)
for i in range(0,len(mlist)):
    for j in range(0,len(rlist)):
        t1d[i,j]=solmatch[t1q[i,j]]
print('total demand 1 = '+str(sum(t1d)))
t2d = []
t2d=creasym(t2d,'t2d',rlist,blist)
for i in range(0,len(rlist)):
    for j in range(0,len(blist)):
        t2d[i,j]=solmatch[t2q[i,j]]
print('total demand 2 = '+str(sum(t2d)))
dd=[]
dd=creasym2(dd,'dd',blist)
for i in range(0,len(blist)):
    dd[i]=d[i].subs(solmatch)
print('total demand 3 = '+str(sum(dd)))

# profits and consumer surplus
profitm=[]
creasym2(profitm,'profitm',mlist)
for i in range(0,len(mlist)):
    profitm[i] = (sum((pm[i,:])*(t1d[i,:]))-f[i]-sum(t1c[i,:])).subs(solmatch)
print('manufacturer profit ='+str(profitm))
profitr=[]
creasym2(profitr,'profitr',rlist)
for i in range(0,len(rlist)):
    profitr[i] = (pr[i]*sum(t2q[i,:])-sum((pm[:,i])*(t1q[:,i]))-c[i]).subs(solmatch)
print('retailer profit ='+str(profitr))
cs=[]
creasym2(cs,'cs',blist)
for i in range(0,len(blist)):
    cs[i] = 0.5*(dd[i])**2
print('consumer surplus ='+str(cs))