# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:11:53 2019

@author: chauman.fung@kuleuven.be
"""
import numpy as np

# set starting values
#list0 = np.ones_like(orglist) 
#list0 = np.ones((m-1)*(r-1)+(r-1)*(b-1)+(r-1)+(b-1))

#list0 = [11,11,11,11] #example 2.1
#list0 = [11,11,11,11,11,11,11] #example 2.2
#list0 = [11,11,11,11,11,11] #example 2.3
#list0 = [11,11,11,11,11,11] #dxample 2.4
#list0 = np.ones(2*2+2*2+2+2) #example 2.5, 2.6
#list0 = np.ones(2*3+3*2+3+2) #example 2.7
list0 = np.ones(3*2+2*3+2+3) #example 2.8


# set alpha
alpha=0.05 #example 2.1,2.2,2.3,2.4,2.5,2.6,2.8
#alpha=0.03 #example 2.7


# set stopping criteria
epsilon = 0.0001

# set max iterations
maxiter=3000