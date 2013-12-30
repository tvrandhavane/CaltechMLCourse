'''
Created on Dec 29, 2013

@author: Tanmay
'''
import numpy as np
from sklearn import svm

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

def generateData(N):
    f = generateTargetFunction()
    X = generateX(N)
    Y = generateY(X, f, N) 
    validData = 0
    for i in Y:
        if i == -1:
            validData = 1
    if validData != 0:
        validData = 0
        for i in Y:
            if i == 1:
                validData = 1
        if validData == 1:
            return [f, X, Y]
        else:
            return generateData(N)
    else:
        return generateData(N)

def pla(X, Y, N):
    g = np.array([0,0,0])
    iterationCount = 1
    for i in range(N):
        x = X[i]
        temp = evaluateF(g, x)
        if temp != Y[i] :
            iterationCount = iterationCount + 1
            g = g + Y[i]*x
            i = 0
    return g        
        
def evaluateDisagreement(g, f, N):
    X = generateX(N)
    Y = generateY(X, f, N)
    count = 0
    for i in range(N):
        if evaluateF(g, X[i]) != Y[i]:
            count = count + 1
    return count/(N*1.0)

def executesvm(X, Y, f, N):
    clf = svm.SVC( kernel='linear')
    clf.fit(X, Y)
    X = generateX(N)
    Y = generateY(X, f, N)
    nsupport = clf.support_vectors_.shape[0]
    count = 0
    for i in range(N):
        if clf.predict(X[i]) != Y[i]:
            count = count + 1
    return [count/(N*1.0), nsupport]
                     
def experiment():
    N = 100
    [f, X, Y] = generateData(N)
    g = pla(X, Y, N)
    plaErr = evaluateDisagreement(g, f, 10000)
    [svmErr, nsupport] = executesvm(X, Y, f, 10000)
    return [plaErr, svmErr, nsupport]
    
def mainFunction():
    count = 0
    totsupport = 0
    for i in range(1000):
        print "Run =", i
        print "Count =", count        
        [plaErr, svmErr, nsupport] = experiment()
        totsupport = totsupport + nsupport 
        if svmErr < plaErr:
            count = count + 1
    print count
    print totsupport
mainFunction()

