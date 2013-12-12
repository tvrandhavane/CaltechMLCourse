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

def calculateEin(X, Y, g, size):
    Ein = (np.dot(X, g.T) - Y)
    sum = 0
    for i in range(size):
        if evaluateG(g, X[i]) != Y[i]:
            sum = sum + Ein[i]*Ein[i]
    sum = sum / size
    return sum

def experiment(N):
    X = generateX(N)
    Y = generateY(X, N)
    noiseIndices = getNoiseIndices(N)
    Ynoisy = generateNoise(Y, noiseIndices)
    XDagger = getXDagger(X)
    g = np.dot(XDagger, Ynoisy).T
    return g
    
def mainFunction():
    runs = 1000
    N = 1000
    gTotal = 0
    for i in range(runs):
        print "run :", i  
        gTotal = gTotal + experiment(N)
    print "g =", gTotal/1000
    
mainFunction()
