'''
Created on Dec 12, 2013

@author: Tanmay
'''
import numpy as np

def generateX(size):
    X = []
    for i in range(size):
        x1 = np.random.uniform(-1,1)
        x2 = np.random.uniform(-1,1) 
        X.append([1, x1, x2, x1*x2, x1*x1, x2*x2])
    Xmatrix = np.array(X)
    return Xmatrix

def getXDagger(X):    
    XDagger = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)
    return XDagger

def evaluateF(x):
    value = x[1]*x[1] + x[2]*x[2] - 0.6
    if value < 0:
        return -1
    elif value >= 0:
        return 1

def evaluateG(g, x):
    value = np.dot(g,x)
    if value <= 0:
        return -1
    else:
        return 1
    
def generateY(X, N):
    temp = []
    for i in range(N):
        temp.append(evaluateF(X[i]))
    Y = np.array(temp)
    return Y

def getNoiseIndices(N):
    noiseIndices = list(range(N))
    np.random.shuffle(noiseIndices)
    noiseIndices = noiseIndices[0:N/10]  
    return noiseIndices
 
def generateNoise(Y, noiseIndices):
    for i in noiseIndices:
        Y[i] = -1*Y[i]
    return Y

def experiment(N):
    X = generateX(N)
    Y = generateY(X, N)
    noiseIndices = getNoiseIndices(N)
    Ynoisy = generateNoise(Y, noiseIndices)
    XDagger = getXDagger(X)
    g = np.dot(XDagger, Ynoisy).T
    
    #estimate Eout
    Xout = generateX(1000)
    Yout = generateY(Xout, 1000)
    noiseIndicesOut = getNoiseIndices(1000)
    YOutnoisy = generateNoise(Yout, noiseIndicesOut)
    count = 0
    for i in range(1000):
        Yest = evaluateG(g, Xout[i])
        if Yest != YOutnoisy[i]:
            count = count + 1
    return count
    
def mainFunction():
    runs = 1000
    N = 1000
    totalCount = 0
    for i in range(runs):
        print "run :", i  
        totalCount = totalCount + experiment(N)
    print "Total Eout =", totalCount
    
mainFunction()
