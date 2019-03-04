# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:59:26 2019

@author: chauman.fung@kuleuven.be
"""
import itertools
import numpy as np
from sympy import *
from varfunc_eg8 import *
from starting import *

L1f = list(itertools.chain.from_iterable(L1))
L2f = list(itertools.chain.from_iterable(L2))
L = [L1f,L2f,L3,L4]
L = list(itertools.chain.from_iterable(L))

t1qf = list(itertools.chain.from_iterable(t1q)) 
t2qf = list(itertools.chain.from_iterable(t2q))
orglist = [t1qf,t2qf,gamma,rho3]
orglist = list(itertools.chain.from_iterable(orglist))

t1qsub=[]
for i in range(1,m):
    for j in range(1,r):
       t1qsub.append(symbols('t1qsub'+str(i)+str(j)))
t1qsub=np.reshape(t1qsub,(m-1,r-1))
t2qsub=[]
for i in range(1,r):
    for j in range(1,b):
       t2qsub.append(symbols('t2qsub'+str(i)+str(j)))
t2qsub=np.reshape(t2qsub,(r-1,b-1))
rho3sub=[]
for i in range(1,b):
    rho3sub.append(symbols('rho3sub'+str(i)))
gammasub=[]
for i in range(1,r):
    gammasub.append(symbols('gammasub'+str(i)))


sublist = []
for i in range(0,m-1):
    for j in range(0,r-1):
        sublist.append(t1qsub[i,j])
for i in range(0,r-1):
    for j in range(0,b-1):
        sublist.append(t2qsub[i,j])
for i in range(0,r-1):
        sublist.append(gammasub[i])
for i in range(0,b-1):
        sublist.append(rho3sub[i])
t1qsubf = list(itertools.chain.from_iterable(t1qsub)) 
t2qsubf = list(itertools.chain.from_iterable(t2qsub))
sublist = [t1qsubf,t2qsubf,gammasub,rho3sub]
sublist = list(itertools.chain.from_iterable(sublist))       
       
# create a substitution function for all
def sub_all(ele,sublist):
    Ltemp=Function('Ltemp')
    Ltemp=L[ele].subs(orglist[0],sublist[0])
    for i in range(1,len(L)):
        Ltemp=Ltemp.subs(orglist[i],sublist[i])
    return Ltemp


def L_sub_all(sublist):
    Lsub=[]  
    for j in range(0,len(L)):
        Lsub.append(Function('Lsub'+str(j)))
        Lsub[j]=sub_all(j,sublist)
    return Lsub



oplist =np.ones((m-1)*(r-1)+(r-1)*(b-1)+(r-1)+(b-1))
  

oplist1 = np.ones((m-1)*(r-1)+(r-1)*(b-1)+(r-1)+(b-1))


def compare2(sublist):
    for i in range(0,len(L)):
        Llist = L_sub_all(sublist)
        oplist[i] = Max(0, sublist[i] - alpha*Llist[i])
    return oplist

def compare3(sublist):
    for i in range(0,len(L)):
        step2 = compare2(sublist)
        Lstep2=L_sub_all(step2)
        oplist1[i] = Max(0, sublist[i] - alpha*Lstep2[i])
    return oplist1



