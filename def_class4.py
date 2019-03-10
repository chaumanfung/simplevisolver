# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:50:37 2019

@author: chauman.fung@kuleuven.be
"""

import itertools
from itertools import count
from sympy import diff,symbols,Function,Max
import numpy as np
from starting import alpha

# construct classes
# manufacturers
class Make(object):
    _ids = count(0)
    def __init__(self, name, supplyto):
        self.name = name
        self.supplyto = supplyto
        self.id = next(self._ids)
        
# retailers
class Retail(object):
    _ids = count(0)
    def __init__(self, name, sellto):
        self.name = name
        self.sellto = sellto
        self.id = next(self._ids)
        
# buyers (markets)
class Buy(object):
    _ids = count(0)
    def __init__(self, name):
        self.name = name
        self.id = next(self._ids)
########################################################################
### edit relationship between manfacturers, retailers and markets here
########################################################################
mlist = []
mlist.append(Make('m1','r1'))
rlist = []
rlist.append(Retail('r1',('b1','b2')))
blist = []
blist.append(Buy('b1'))
blist.append(Buy('b2'))

# define function for creating symbols
def creasym(name,place,row,column):
    for i in range(1,len(row)+1):
        for j in range(1,len(column)+1):
            name.append(symbols(str(place)+str(i)+str(j)))
    name=np.reshape(name,(len(row),len(column)))
    return name

def creasym2(name,place,row):
    for i in range(1,len(row)+1):
        name.append(symbols(str(place)+str(i)))
    return name

# define function for creating functions
def creafun(name,place,row,column):
    for i in range(1,len(row)+1):
        for j in range(1,len(column)+1):
            name.append(Function(str(place)+str(i)+str(j)))
    name=np.reshape(name,(len(row),len(column)))
    return name

def creafun2(name,place,row):
    for i in range(1,len(row)+1):
        name.append(Function(str(place)+str(i)))
    return name

# definitions
t1q=[]
t1q=creasym(t1q,'t1q',mlist,rlist)

t2q=[]
t2q=creasym(t2q,'t2q',rlist,blist)

gamma=[]
gamma=creasym2(gamma,'gamma',rlist)

rho3=[]
rho3=creasym2(rho3,'rho3',blist)

f=[]
f=creafun2(f,'f',mlist)

t1c=[]
t1c=creafun(t1c,'t1c',mlist,rlist)

c=[]
c=creafun2(c,'c',rlist)

d=[]
d=creafun2(d,'d',blist)

t2c=[]
t2c=creafun(t2c,'t2c',rlist,blist)


##############################################################
## edit production cost functions here
##############################################################

f[0] = 1*(t1q[0,0])**2 + 5*(t1q[0,0]) 

##############################################################
##############################################################
## edit transaction cost faced by manufactuerers here
##############################################################
t1c[0,0] = (t1q[0,0] +2)*t1q[0,0]

############################################################
############################################################
## edit handling cost of retailers here
############################################################
c[0] = 2*(np.sum([t1q[:,0]]))**2

############################################################
############################################################
## edit demand functions here    
############################################################
d[0] = -1*rho3[0] + 100
d[1] = -1*rho3[1] + 100
############################################################
############################################################
## edit transaction costs between retailers and consumers
###########################################################
t2c[0,0] = 1*t2q[0,0] + 1
t2c[0,1] = 1*t2q[0,1] + 1
########################################################### 

# the F function 

L1=[]
L1=creafun(L1,'L1',mlist,rlist)
L1=np.reshape(L1,(len(mlist),len(rlist)))

for i in range(0,len(mlist)):
    for j in range(0,len(rlist)):
        L1[i,j] = (f[i].diff(t1q[i,j]) + t1c[i,j].diff(t1q[i,j]) 
        + c[j].diff(t1q[i,j]) - gamma[j])

L2=[]
L2=creafun(L2,'L2',rlist,blist)
L2=np.reshape(L2,(len(rlist),len(blist)))

for i in range(0,len(rlist)):
    for j in range(0,len(blist)):
        L2[i,j] = (t2c[i,j] + gamma[i] - rho3[j])

L3=[]
L3=creafun2(L3,'L3',rlist)
for i in range(0,len(rlist)):
    L3[i] = np.sum(t1q[:,i])-np.sum(t2q[i,:])

L4=[]
L4=creafun2(L4,'L4',blist)
for i in range(0,len(blist)):
    L4[i] = (np.sum(t2q[:,i]) - d[i])       


L1f = list(itertools.chain.from_iterable(L1))
L2f = list(itertools.chain.from_iterable(L2))
L = [L1f,L2f,L3,L4]
L = list(itertools.chain.from_iterable(L))

t1qf = list(itertools.chain.from_iterable(t1q)) 
t2qf = list(itertools.chain.from_iterable(t2q))
orglist = [t1qf,t2qf,gamma,rho3]
orglist = list(itertools.chain.from_iterable(orglist))

t1qsub=[]
t1qsub=creasym(t1qsub,'t1qsub',mlist,rlist)
t2qsub=[]
t2qsub=creasym(t2qsub,'t2qsub',rlist,blist)
rho3sub=[]
rho3sub=creasym2(rho3sub,'rho3sub',blist)
gammasub=[]
gammasub=creasym2(gammasub,'gammasub',rlist)

sublist = []
t1qsubf = list(itertools.chain.from_iterable(t1qsub)) 
t2qsubf = list(itertools.chain.from_iterable(t2qsub))
sublist = [t1qsubf,t2qsubf,gammasub,rho3sub]
sublist = list(itertools.chain.from_iterable(sublist))       

oplist =np.ones(len(L))
oplist1 = np.ones(len(L))
      
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
