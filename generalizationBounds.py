'''
Created on Dec 20, 2013

@author: Tanmay
'''

import math

def computeVCBound(dvc, delta, N):
    value = math.sqrt((((dvc+2)*math.log(2) + dvc*math.log(N) - math.log(delta))*8)/N)
    return value    

def computeRPBound(dvc, delta, N): 
    value = math.sqrt((2*(dvc+1)*math.log(2*N))/N) + math.sqrt((-2*math.log(delta))/N) + 1/N
    return value 

def computePvBBound(dvc, delta, N): 
    #ignore eps term for large value of N
    value = math.sqrt((math.log(6) + dvc*math.log(2*N) - math.log(delta))/N)
    return value

def computeDBound(dvc, delta, N): 
    #ignore eps term for large value of N
    value = math.sqrt((math.log(4) + 2*dvc*math.log(N) - math.log(delta))/(2*N))
    return value
  
def mainFunction():
    dvc = 50
    delta = 0.05
    print computeVCBound(dvc, delta, 5)
    print computeRPBound(dvc, delta, 5)
    print computePvBBound(dvc, delta, 5)
    print computeDBound(dvc, delta, 5)   
    
mainFunction()