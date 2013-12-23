'''
Created on Dec 23, 2013

@author: Tanmay
'''
import numpy as np
import math

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

def computeGradient(x, y, w):
    warr = np.array(w)
    err = y*np.dot(warr.T, x)
    if err < 700:
        err = 1 + math.exp(err)
        return (y/err)*x
    else:
        return 0
    

def generateEpoch(size):
    x = range(100)
    np.random.shuffle(x)
    return x

def computeDistance(w1, w2):
    dist = 0
    i = 0
    while i < w1.size:
        dist = dist + (w1[i] - w2[i])*(w1[i] - w2[i])
        i = i + 1
    return math.sqrt(dist)   

def crossEntropyError(x, y, w):
    err = -y*np.dot(w.T, x)
    err = 1 + math.exp(err)
    return math.log(err)

def evaluateEout(w, f):
    N = 100000
    X = generateX(N)
    Y = generateY(X, f, N)
    error = 0
    for i in range(N):
        error = error + crossEntropyError(X[i], Y[i], w)
    return error/N
        
def experiment():
    N = 100
    eta = 0.01
    X = generateX(N)
    f = generateTargetFunction()
    Y = generateY(X, f, N)
    wprev = [0, 0, 0]
    flag = 1
    epochCount = 0
    while flag==1:
        epoch = generateEpoch(N)
        w = wprev
        epochCount = epochCount + 1
        for i in epoch:
            grad = computeGradient(X[i], Y[i], w) 
            w = w + eta*grad
        dist = computeDistance(w, wprev)
        wprev = w
        if dist < 0.01:
            flag = 0    
    return epochCount

def mainFunction():
    runs = 100
    epochs = 0
    for i in range(runs):
        print "Iteration Number =", i+1
        epochs = epochs + experiment()
    print epochs/runs

mainFunction()