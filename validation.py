'''
Created on Dec 28, 2013

@author: Tanmay
'''
import numpy as np

def readFile(name):
    f = open(name, "r")
    Xtemp = []
    Ytemp = []
    for line in f:
        numbers = line.split()
        Xtemp.append([float(numbers[0]), float(numbers[1])])
        Ytemp.append(float(numbers[2]))
    X = np.array(Xtemp)
    Y = np.array(Ytemp)
    return [X, Y]

def splitSet(X, Y, p, q):
    Xtemp = []
    Ytemp = []
    for i in range(p):
        Xtemp.append(X[i])
        Ytemp.append(Y[i])
    Xtrain = np.array(Xtemp)
    Ytrain = np.array(Ytemp)
    Xtemp = []
    Ytemp = []
    for i in range(q):
        Xtemp.append(X[i+p])
        Ytemp.append(Y[i+p])
    Xval = np.array(Xtemp)
    Yval = np.array(Ytemp)
    return [Xtrain, Ytrain, Xval, Yval]

def generateZ(X):
    Ztemp = []
    for i in X :
        x1 = i[0]
        x2 = i[1]
        Ztemp.append([1, x1, x2, x1*x1, x2*x2, x1*x2, abs(x1 - x2), abs(x1 + x2)])
    Z = np.array(Ztemp)
    return Z

def getXDagger(X):    
    XDagger = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)
    return XDagger

def linearRegression(Z, Y):
    Zdagger = getXDagger(Z)
    w = np.dot(Zdagger, Y).T
    return w

def getModelZ(Z, q):
    ztemp = []
    for i in Z:
        ztemp.append(i[0:q+1])
    return np.array(ztemp)

def computeError(Z, Y, w):
    count = 0
    for i in range(Z.shape[0]):
        value = Y[i]*np.dot(w.T, Z[i])
        if value <= 0:
            count = count + 1
    return count/(Z.shape[0]*1.0)

def computeErrorExperiment1(Zin, Yin, Zout, Yout, q):
    Z1 = getModelZ(Zin, q)
    [Z1train, Ytrain, Z1Val, YVal] = splitSet(Z1, Yin, 25, 10)
    w1 = linearRegression(Z1train, Ytrain)
    errorIn = computeError(Z1Val, YVal, w1)
    Z1 = getModelZ(Zout, q)
    errorOut = computeError(Z1, Yout, w1)
    return [errorIn, errorOut]

def experiment1():
    [Xin, Yin] = readFile("hw06in.dta")
    Zin = generateZ(Xin)  
    
    [Xout, Yout] = readFile("hw06out.dta")
    Zout = generateZ(Xout)
    
    print "Error 1=", computeErrorExperiment1(Zin, Yin, Zout, Yout, 3)
    print "Error 2=", computeErrorExperiment1(Zin, Yin, Zout, Yout, 4)
    print "Error 3=", computeErrorExperiment1(Zin, Yin, Zout, Yout, 5)
    print "Error 4=", computeErrorExperiment1(Zin, Yin, Zout, Yout, 6)
    print "Error 5=", computeErrorExperiment1(Zin, Yin, Zout, Yout, 7)

def computeErrorExperiment2(Zin, Yin, Zout, Yout, q):
    Z1 = getModelZ(Zin, q)
    [Z1train, Ytrain, Z1Val, YVal] = splitSet(Z1, Yin, 10, 25)
    w1 = linearRegression(Z1train, Ytrain)
    errorIn = computeError(Z1Val, YVal, w1)
    Z1 = getModelZ(Zout, q)
    errorOut = computeError(Z1, Yout, w1)
    return [errorIn, errorOut]

def experiment2():
    [Xin, Yin] = readFile("hw06in.dta")
    Zin = generateZ(Xin)  
    
    [Xout, Yout] = readFile("hw06out.dta")
    Zout = generateZ(Xout)
    
    print "Error 1=", computeErrorExperiment2(Zin, Yin, Zout, Yout, 3)
    print "Error 2=", computeErrorExperiment2(Zin, Yin, Zout, Yout, 4)
    print "Error 3=", computeErrorExperiment2(Zin, Yin, Zout, Yout, 5)
    print "Error 4=", computeErrorExperiment2(Zin, Yin, Zout, Yout, 6)
    print "Error 5=", computeErrorExperiment2(Zin, Yin, Zout, Yout, 7)

experiment2()