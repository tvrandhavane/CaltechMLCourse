'''
Created on Dec 20, 2013

@author: Tanmay
'''

#valid for hw04 question 4, 5, 6

import numpy as np
import math

def f(x):
    return math.sin(math.pi*x)

def computea(x1, x2):
    #got by calculation
    a = (x1*f(x1) + x2*f(x2))/(x1*x1 + x2*x2)
    return a

def computeg(a, x):
    return a*x

def generateX(N):
    temp = []
    for i in range(N):
        x1 = np.random.uniform(-1,1)
        x2 = np.random.uniform(-1,1)
        temp.append([x1, x2])
    X = np.array(temp)
    return X

def computeExpecteda(X):
    temp = []
    for i in X:
        temp.append(computea(i[0], i[1]))
    A = np.array(temp)
    return A.mean()

def computeBias(aEx, N):
    temp = []
    for i in range(N):
        x = np.random.uniform(-1, 1)
        gx = computeg(aEx, x)
        fx = f(x)
        sqErr = (gx - fx)*(gx - fx)
        temp.append(sqErr)
    sqError = np.array(temp)
    return sqError.mean()

def computeVariance(aEx, X):
    #variance = Expected over x[Expected over a[(ax - aEx x)^2]]
    # = expected over x[(expected over a (a - aEx)^2) * x^2]
    # c = (expected over a (a - aEx)^2)
    # variance = c * expected over x[x^2]
    # = c/3
    temp = []
    for i in X:
        a = computea(i[0], i[1])
        temp.append((a - aEx)*(a - aEx))
    A = np.array(temp)
    return A.mean()/3
 
def mainFunction():        
    N = 10000
    X = generateX(N)
    aEx = computeExpecteda(X)
    bias = computeBias(aEx, N)
    variance = computeVariance(aEx, X)
    print variance
    
mainFunction()
    