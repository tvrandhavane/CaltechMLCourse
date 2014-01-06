'''
Created on Dec 29, 2013

@author: Tanmay
'''
import numpy as np
from sklearn import svm
from sklearn.cross_validation import KFold

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

def evalCLF1(Xtrain, Ytrain, C, Q, n):
	YtrainToUse = xvsAll(Ytrain, n)

	clf = svm.SVC( kernel='poly', C=C, coef0=1, degree=Q, gamma=1.0)
   	clf.fit(Xtrain, YtrainToUse)

   	error = 0
   	for i in range(YtrainToUse.shape[0]):
		if(clf.predict(Xtrain[i]) != YtrainToUse[i]):
   			error = error + 1
   	return error/(YtrainToUse.shape[0]*1.0) 

def experiment1():
	C = 0.01
	Q = 2
	[Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")

	print "Error 0 =", evalCLF1(Xtrain, Ytrain, C, Q, 0)
	print "Error 2 =", evalCLF1(Xtrain, Ytrain, C, Q, 2)
	print "Error 4 =", evalCLF1(Xtrain, Ytrain, C, Q, 4)
	print "Error 6 =", evalCLF1(Xtrain, Ytrain, C, Q, 6)
	print "Error 8 =", evalCLF1(Xtrain, Ytrain, C, Q, 8)
	print "Error 1 =", evalCLF1(Xtrain, Ytrain, C, Q, 1)
	print "Error 3 =", evalCLF1(Xtrain, Ytrain, C, Q, 3)
	print "Error 5 =", evalCLF1(Xtrain, Ytrain, C, Q, 5)
	print "Error 7 =", evalCLF1(Xtrain, Ytrain, C, Q, 7)
	print "Error 9 =", evalCLF1(Xtrain, Ytrain, C, Q, 9)

def evalCLF2(Xtrain, Ytrain, C, Q, n):
	YtrainToUse = xvsAll(Ytrain, n)

	clf = svm.SVC( kernel='poly', C=C, coef0=1, degree=Q, gamma=1.0)
   	clf.fit(Xtrain, YtrainToUse)
   	return clf.support_vectors_.shape[0]

def experiment2():
	C = 0.01
	Q = 2
	[Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")

	print "SV 0 =", evalCLF2(Xtrain, Ytrain, C, Q, 0)
	print "SV 1 =", evalCLF2(Xtrain, Ytrain, C, Q, 1)

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

def evalCLF3(Xtrain, Ytrain, Xtest, Ytest, C, Q):
	[XtrainToUse, YtrainToUse] = onevsFive(Xtrain, Ytrain)
	[XtestToUse, YtestToUse] = onevsFive(Xtest, Ytest)

	clf = svm.SVC( kernel='poly', C=C, coef0=1, degree=Q, gamma=1.0)
   	clf.fit(XtrainToUse, YtrainToUse)

   	error = 0
   	for i in range(YtrainToUse.shape[0]):
		if(clf.predict(XtrainToUse[i]) != YtrainToUse[i]):
   			error = error + 1
   	ein = error/(YtrainToUse.shape[0]*1.0) 

   	error = 0
   	for i in range(YtestToUse.shape[0]):
		if(clf.predict(XtestToUse[i]) != YtestToUse[i]):
   			error = error + 1
   	eout = error/(YtestToUse.shape[0]*1.0)

   	nsupport = clf.support_vectors_.shape[0]
   	return [ein, eout, nsupport]

def experiment3():
	Q = 5
	[Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")
	[Xtest, Ytest] = readFile("hw08featuresTrain.txt")

	print "C 0.0001 =", evalCLF3(Xtrain, Ytrain, Xtest, Ytest, 0.001, Q)
	print "C 0.001 =", evalCLF3(Xtrain, Ytrain, Xtest, Ytest, 0.001, Q)
	print "C 0.01 =", evalCLF3(Xtrain, Ytrain, Xtest, Ytest, 0.01, Q)
	print "C 0.1 =", evalCLF3(Xtrain, Ytrain, Xtest, Ytest, 0.1, Q)
	print "C 1 =", evalCLF3(Xtrain, Ytrain, Xtest, Ytest, 1, Q)

def evalCLF4(Xtrain, Ytrain, C, Q):
	[XtrainToUse, YtrainToUse] = onevsFive(Xtrain, Ytrain)

	kf = KFold(len(YtrainToUse), n_folds=10, shuffle=True)
	ecv = 0
	n = 0
	for train_index, test_index in kf:
		n = n + 1
		X_train, X_test = XtrainToUse[train_index], XtrainToUse[test_index]
		y_train, y_test = YtrainToUse[train_index], YtrainToUse[test_index]

		clf = svm.SVC( kernel='poly', C=C, coef0=1, degree=Q, gamma=1.0)
   		clf.fit(X_train, y_train)

	   	error = 0
	   	for i in range(y_test.shape[0]):
			if(clf.predict(X_test[i]) != y_test[i]):
	   			error = error + 1
	   	ecv = ecv + error/(y_test.shape[0]*1.0)
	return ecv/(n * 1.0)

def experiment4():
	Q = 2
	[Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")

	count = [0, 0, 0, 0, 0]
	error = 0
	for i in range(100):
		print "run =", i
		e = []
		e.append(evalCLF4(Xtrain, Ytrain, 0.0001, Q))
		e.append(evalCLF4(Xtrain, Ytrain, 0.001, Q))
		e.append(evalCLF4(Xtrain, Ytrain, 0.01, Q))
		e.append(evalCLF4(Xtrain, Ytrain, 0.1, Q))
		e.append(evalCLF4(Xtrain, Ytrain, 1, Q))
		error = error + e[2]
		ind = np.argmin(e)
		count[ind] = count[ind] + 1
	print count
	print error/100

def evalCLF5(Xtrain, Ytrain, Xtest, Ytest, C):
	[XtrainToUse, YtrainToUse] = onevsFive(Xtrain, Ytrain)
	[XtestToUse, YtestToUse] = onevsFive(Xtest, Ytest)

	clf = svm.SVC( kernel='rbf', C=C, gamma=1.0)
   	clf.fit(XtrainToUse, YtrainToUse)

   	error = 0
   	for i in range(YtrainToUse.shape[0]):
		if(clf.predict(XtrainToUse[i]) != YtrainToUse[i]):
   			error = error + 1
   	ein = error/(YtrainToUse.shape[0]*1.0) 

   	error = 0
   	for i in range(YtestToUse.shape[0]):
		if(clf.predict(XtestToUse[i]) != YtestToUse[i]):
   			error = error + 1
   	eout = error/(YtestToUse.shape[0]*1.0)

   	return [ein, eout]

def experiment5():
	Q = 5
	[Xtrain, Ytrain] = readFile("hw08featuresTrain.txt")
	[Xtest, Ytest] = readFile("hw08featuresTest.txt")

	print "C 0.01 =", evalCLF5(Xtrain, Ytrain, Xtest, Ytest, 0.01)
	print "C 1 =", evalCLF5(Xtrain, Ytrain, Xtest, Ytest, 1)
	print "C 100 =", evalCLF5(Xtrain, Ytrain, Xtest, Ytest, 100)
	print "C 10000 =", evalCLF5(Xtrain, Ytrain, Xtest, Ytest, 10000)
	print "C 1000000 =", evalCLF5(Xtrain, Ytrain, Xtest, Ytest, 1000000)

experiment5()