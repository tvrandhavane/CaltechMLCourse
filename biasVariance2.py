'''
Created on Dec 20, 2013

@author: Tanmay
'''

#valid for hw04 question 7

import numpy as np
import math

def f(x):
    return math.sin(math.pi*x)

def computeaA(x1, x2):
    #differentiate squared error wrt a
    a = (f(x1) + f(x2))/2
    return a

def computeaB(x1, x2):
    #differentiate squared error wrt a
    a = (x1*f(x1) + x2*f(x2))/(x1*x1 + x2*x2)
    return a

def computeaC(x1, x2):
    #line passing through x1 and x2
    a = (f(x1) - f(x2)) / (x1 - x2)
    b = (x1*f(x2) - x2*f(x1)) / (x1 - x2)
    return [a, b]

def computeaD(x1, x2):
    #differentiate squared error wrt a
    a = (x1*x1*f(x1) + x2*x2*f(x2))/(x1*x1*x1*x1 + x2*x2*x2*x2)
    return a

def computeaE(x1, x2):
    #line passing through x1^2 and x2^2
    a = (f(x1) - f(x2)) / (x1*x1 - x2*x2)
    b = (x1*x1*f(x2) - x2*x2*f(x1)) / (x1*x1 - x2*x2)
    return [a, b]

def computegA(a, x):
    return a

def computegB(a, x):
    return a*x

def computegC(a, x):
    return a[0]*x + a[1]

def computegD(a, x):
    return a*x*x

def computegE(a, x):
    return a[0]*x*x + a[1]

def generateX(N):
    temp = []
    for i in range(N):
        x1 = np.random.uniform(-1,1)
        x2 = np.random.uniform(-1,1)
        temp.append([x1, x2])
    X = np.array(temp)
    return X

def computeExpectedaA(X):
    temp = []
    for i in X:
        temp.append(computeaA(i[0], i[1]))
    A = np.array(temp)
    return A.mean()

def computeExpectedaB(X):
    temp = []
    for i in X:
        temp.append(computeaB(i[0], i[1]))
    A = np.array(temp)
    return A.mean()

def computeExpectedaC(X):
    temp = []
    for i in X:
        temp.append(computeaC(i[0], i[1]))
    A = np.array(temp)
    return [A[:,0].mean(), A[:,0].mean()]

def computeExpectedaD(X):
    temp = []
    for i in X:
        temp.append(computeaD(i[0], i[1]))
    A = np.array(temp)
    return A.mean()

def computeExpectedaE(X):
    temp = []
    for i in X:
        temp.append(computeaE(i[0], i[1]))
    A = np.array(temp)
    return [A[:,0].mean(), A[:,0].mean()]

def computeBiasA(aEx, N):
    temp = []
    for i in range(N):
        x = np.random.uniform(-1, 1)
        gx = computegA(aEx, x)
        fx = f(x)
        sqErr = (gx - fx)*(gx - fx)
        temp.append(sqErr)
    sqError = np.array(temp)
    return sqError.mean()

def computeBiasB(aEx, N):
    temp = []
    for i in range(N):
        x = np.random.uniform(-1, 1)
        gx = computegB(aEx, x)
        fx = f(x)
        sqErr = (gx - fx)*(gx - fx)
        temp.append(sqErr)
    sqError = np.array(temp)
    return sqError.mean()

def computeBiasC(aEx, N):
    temp = []
    for i in range(N):
        x = np.random.uniform(-1, 1)
        gx = computegC(aEx, x)
        fx = f(x)
        sqErr = (gx - fx)*(gx - fx)
        temp.append(sqErr)
    sqError = np.array(temp)
    return sqError.mean()

def computeBiasD(aEx, N):
    temp = []
    for i in range(N):
        x = np.random.uniform(-1, 1)
        gx = computegD(aEx, x)
        fx = f(x)
        sqErr = (gx - fx)*(gx - fx)
        temp.append(sqErr)
    sqError = np.array(temp)
    return sqError.mean()

def computeBiasE(aEx, N):
    temp = []
    for i in range(N):
        x = np.random.uniform(-1, 1)
        gx = computegE(aEx, x)
        fx = f(x)
        sqErr = (gx - fx)*(gx - fx)
        temp.append(sqErr)
    sqError = np.array(temp)
    return sqError.mean()

def computeVarianceA(aEx, X):
    #variance = Expected over x[Expected over a[(ax - aEx)^2]]
    # = expected over x[(expected over a (a - aEx)^2)]
    # c = (expected over a (a - aEx)^2)
    # variance = c
    temp = []
    for i in X:
        a = computeaA(i[0], i[1])
        temp.append((a - aEx)*(a - aEx))
    A = np.array(temp)
    return A.mean()

def computeVarianceB(aEx, X):
    #variance = Expected over x[Expected over a[(ax - aEx x)^2]]
    # = expected over x[(expected over a (a - aEx)^2) * x^2]
    # c = (expected over a (a - aEx)^2)
    # variance = c * expected over x[x^2]
    # = 2c/3
    temp = []
    for i in X:
        a = computeaB(i[0], i[1])
        temp.append((a - aEx)*(a - aEx))
    A = np.array(temp)
    return A.mean()/3

def computeVarianceC(aEx, X):
    temp = []
    for i in X:
        a = computeaC(i[0], i[1])
        c1 = (1/3)*(a[0] - aEx[0])*(a[0] - aEx[0])
        c2 = (a[1] - aEx[1])*(a[1] - aEx[1])
        temp.append(c1+c2)
    A = np.array(temp)
    return A.mean()

def computeVarianceD(aEx, X):
    #variance = Expected over x[Expected over a[(ax - aEx x)^2]]
    # = expected over x[(expected over a (a - aEx)^2) * x^2]
    # c = (expected over a (a - aEx)^2)
    # variance = c * expected over x[x^2]
    # = 2c/3
    temp = []
    for i in X:
        a = computeaD(i[0], i[1])
        temp.append((a - aEx)*(a - aEx))
    A = np.array(temp)
    return A.mean()/5

def computeVarianceE(aEx, X):
    temp = []
    for i in X:
        a = computeaC(i[0], i[1])
        c1 = (1/5)*(a[0] - aEx[0])*(a[0] - aEx[0])
        c2 = (a[1] - aEx[1])*(a[1] - aEx[1])
        temp.append(c1+c2)
    A = np.array(temp)
    return A.mean()
 
def mainFunction():        
    N = 10000
    X = generateX(N)
        
    aExA = computeExpectedaA(X)
    biasA = computeBiasA(aExA, N)
    varianceA = computeVarianceA(aExA, X)
    print "A =", biasA+varianceA
    
    aExB = computeExpectedaB(X)
    biasB = computeBiasB(aExB, N)
    varianceB = computeVarianceB(aExB, X)
    print "B =", biasB+varianceB
    
    aExC = computeExpectedaC(X)
    biasC = computeBiasC(aExC, N)
    varianceC = computeVarianceC(aExC, X)
    print "C =", biasC+varianceC
    
    aExD = computeExpectedaD(X)
    biasD = computeBiasD(aExD, N)
    varianceD = computeVarianceD(aExD, X)
    print "D =", biasD+varianceD
    
    aExE = computeExpectedaE(X)
    biasE = computeBiasE(aExE, N)
    varianceE = computeVarianceE(aExE, X)
    print "E =", biasE+varianceE
    
mainFunction()
    