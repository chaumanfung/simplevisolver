# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:11:53 2019

@author: chauman.fung@kuleuven.be
"""
import numpy as np

# set starting values
#list0 = np.ones_like(orglist) 
#list0 = np.ones((m-1)*(r-1)+(r-1)*(b-1)+(r-1)+(b-1))
#list0 = np.ones(2*2+2*2+2+2) #example 1 and 2
#list0 = np.ones(2*3+3*2+3+2) #example 3
list0 = np.ones(3*2+2*3+2+3) #example 4
#list0 = [11,11,11,11,11,11]

# set alpha
#alpha=0.05 #example1 and 2
#alpha=0.03 #example3
alpha=0.05 #example4


# set stopping criteria
epsilon = 0.0001

# set max iterations
maxiter=3000