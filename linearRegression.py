'''
Created on Dec 10, 2013

@author: Tanmay
'''
import numpy as np

def generateRandomPair() :
    pair = [1, 2]
    pair[0] = np.random.uniform(-1,1)
    pair[1] = np.random.uniform(-1,1)
    return pair

def generateTargetFunction():
    X = []
    point1 = generateRandomPair()
    point2 = generateRandomPair()
    f0 = (point1[0]*point2[1] - point2[0]*point1[1]) /  (point1[0] - point2[0])
    f1 = (point1[1] - point2[1]) / (point1[0] - point2[0])
    X.append([f0, f1, -1])
    f = np.array(X)
    return f

def evaluateF(f,x):
    value = np.dot(f,x)
    if value <= 0:
        return -1
    else:
        return 1

def generateX(size):
    X = []
    for i in range(size):
        X.append([1, np.random.uniform(-1,1), np.random.uniform(-1,1)])
    Xmatrix = np.array(X)
    return Xmatrix

def generateY(X, f, size):
    Ytemp = []
    for i in range(size):
        Ytemp.append([evaluateF(f[0], X[i])])
    Y = np.array(Ytemp)
    return Y

def getXDagger(X):    
    XDagger = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)
    return XDagger

def calculateEin(X, Y, g, size):
    Ein = (np.dot(X, g.T) - Y)
    sum = 0
    for i in range(size):
        if evaluateF(g[0], X[i]) != Y[i]:
            sum = sum + Ein[i]*Ein[i]
    sum = sum / size
    return sum

def experiment(N):
    f = generateTargetFunction()
    print "f", f    
    X = generateX(N)
    Y = generateY(X, f, N)
    XDagger = getXDagger(X)
    g = np.dot(XDagger, Y).T
    print "g", g 
    Ein = calculateEin(X, Y, g, N)
    return Ein 
    
def mainFunction():
    runs = 1000
    N = 100
    sumEin = 0
    for i in range(runs):
        print "run :", i  
        sumEin = sumEin + experiment(N)
    print "Total Ein =", sumEin
    
mainFunction()
