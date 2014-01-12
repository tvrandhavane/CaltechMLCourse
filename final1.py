'''
Created on Jan 11, 2013

@author: Tanmay
'''

import numpy as np
import math

def readFile(name):
    f = open(name, "r")
    Ytemp = []
    Xtemp = []
    for line in f:
        numbers = line.split()
        Xtemp.append([float(numbers[1]), float(numbers[2])])
        Ytemp.append(float(numbers[0]))
    X = np.array(Xtemp)
    Y = np.array(Ytemp)
    return [X, Y]

def xvsAll(Y, n):
    Ytemp = []
    for i in Y:
        if i == n:
            Ytemp.append(1)
        else:
            Ytemp.append(-1)
    return np.array(Ytemp)

def onevsFive(X, Y):
    Xtemp = []
    Ytemp = []
    for i in range(Y.shape[0]):
        if Y[i] == 1:
            Xtemp.append(X[i])
            Ytemp.append(1)
        elif Y[i] == 5:
            Xtemp.append(X[i])
            Ytemp.append(-1)
    return [np.array(Xtemp), np.array(Ytemp)]   

def getZ1(X):
    temp = []
    for i in X:
        temp.append([1, i[0], i[1]])
    return np.array(temp)

def getZ2(X):
    temp = []
    for i in X:
        temp.append([1, i[0], i[1], i[0]*i[1], i[0]*i[0], i[1]*i[1]])
    return np.array(temp)

def evalCLF1(Xtrain, Ytrain, lamda, n):
    YtrainToUse = xvsAll(Ytrain, n)

    Z = getZ1(Xtrain)
    w = np.dot(np.dot(np.linalg.inv(np.dot(Z.T, Z) + lamda*np.identity(Z.shape[1])), Z.T), YtrainToUse)

    error = 0
    for i in range(YtrainToUse.shape[0]):
        out = np.dot(w.T, Z[i])
        temp = 0
        if out < 0:
            temp = -1
        else:
            temp = 1
        if (temp != YtrainToUse[i]):
            error = error + 1
    return error/(YtrainToUse.shape[0]*1.0)

def evalCLF3(Xtrain, Ytrain, Xtest, Ytest, lamda):
    [XtrainToUse, YtrainToUse] = onevsFive(Xtrain, Ytrain)
    [XtestToUse, YtestToUse] = onevsFive(Xtest, Ytest)

    Z = getZ2(XtrainToUse)
    Ztest = getZ2(XtestToUse)
    w = np.dot(np.dot(np.linalg.inv(np.dot(Z.T, Z) + lamda*np.identity(Z.shape[1])), Z.T), YtrainToUse)

    error = 0
    for i in range(YtrainToUse.shape[0]):
        out = np.dot(w.T, Z[i])
        temp = 0
        if out < 0:
            temp = -1
        else:
            temp = 1
        if (temp != YtrainToUse[i]):
            error = error + 1

    ein = error/(YtrainToUse.shape[0]*1.0)

    
    error = 0
    for i in range(YtestToUse.shape[0]):
        out = np.dot(w.T, Ztest[i])
        temp = 0
        if out < 0:
            temp = -1
        else:
            temp = 1
        if (temp != YtestToUse[i]):
            error = error + 1
    eout = error/(YtestToUse.shape[0]*1.0)   

    return [ein, eout]

def evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, n):
    YtrainToUse = vsAll(Ytrain, n)

    Z = getZ2(Xtrain)
    w = np.dot(np.dot(np.linalg.inv(np.dot(Z.T, Z) + lamda*np.identity(Z.shape[1])), Z.T), YtrainToUse)

    YtestToUse = xvsAll(Ytest, n)
    Ztest = getZ2(Xtest)
    error = 0
    for i in range(YtestToUse.shape[0]):
        out = np.dot(w.T, Ztest[i])
        temp = 0
        if out < 0:
            temp = -1
        else:
            temp = 1
        if (temp != YtestToUse[i]):
            error = error + 1
    return error/(YtestToUse.shape[0]*1.0)

def experiment1():
    lamda = 1
    [Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")

    print "Error 0 =", evalCLF1(Xtrain, Ytrain, lamda, 0)
    print "Error 1 =", evalCLF1(Xtrain, Ytrain, lamda, 1)
    print "Error 2 =", evalCLF1(Xtrain, Ytrain, lamda, 2)
    print "Error 3 =", evalCLF1(Xtrain, Ytrain, lamda, 3)
    print "Error 4 =", evalCLF1(Xtrain, Ytrain, lamda, 4)
    print "Error 5 =", evalCLF1(Xtrain, Ytrain, lamda, 5)
    print "Error 6 =", evalCLF1(Xtrain, Ytrain, lamda, 6)
    print "Error 7 =", evalCLF1(Xtrain, Ytrain, lamda, 7)
    print "Error 8 =", evalCLF1(Xtrain, Ytrain, lamda, 8)
    print "Error 9 =", evalCLF1(Xtrain, Ytrain, lamda, 9)

def experiment2():
    lamda = 1
    [Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")
    [Xtest, Ytest] = readFile("hw08featuresTest.txt")

    print "Error 0 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 0)
    print "Error 1 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 1)
    print "Error 2 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 2)
    print "Error 3 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 3)
    print "Error 4 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 4)
    print "Error 5 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 5)
    print "Error 6 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 6)
    print "Error 7 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 7)
    print "Error 8 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 8)
    print "Error 9 =", evalCLF2(Xtrain, Ytrain, Xtest, Ytest, lamda, 9)

def experiment3():
    [Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")
    [Xtest, Ytest] = readFile("hw08featuresTest.txt")

    print "Lambda 0.01 =", evalCLF3(Xtrain, Ytrain, Xtest, Ytest, 0.01)
    print "Lambda 1 =", evalCLF3(Xtrain, Ytrain, Xtest, Ytest, 1)

experiment3()