'''
Created on Jan 11, 2013

@author: Tanmay
'''
import numpy as np
from sklearn import svm
from sklearn.cluster import KMeans
import math

def generateTrainingPoints(n):
	Xtemp = []
	Ytemp = []
	for i in range(n):
		x1 = np.random.uniform(-1,1)
		x2 = np.random.uniform(-1,1)
		Xtemp.append([x1, x2])
		yval = x2 - x1 + 0.25*math.sin(math.pi * x1)
		if yval < 0:
			Ytemp.append(-1)
		else:
			Ytemp.append(1)
	return [np.array(Xtemp), np.array(Ytemp)]

def hardMarginSVM(Xtrain, Ytrain, gamma):
	clf = svm.SVC( kernel='rbf', gamma=gamma, C=1000)
   	clf.fit(Xtrain, Ytrain)

   	error = 0
   	for i in range(Ytrain.shape[0]):
   		out = clf.predict(Xtrain[i])
   		if out < 0:
   			value = -1
   		else:
   			value = 1
   		if value != Ytrain[i]:
   			error = error + 1
   	ein = error/(Ytrain.shape[0]*1.0) 
   	return ein

def experiment1():
	runs = 1000
	n = 100
	gamma = 1.5
	count = 0
	for i in range(runs):
		print "Run =", i
		[Xtrain, Ytrain] = generateTrainingPoints(n)
		ein = hardMarginSVM(Xtrain, Ytrain, gamma)
		if ein != 0:
			count = count + 1
	print count/(runs*1.0)

def getw(X, Y, centers, gamma, K):
	matrix = []
	for i in X:
		temp = []
		temp.append(1)
		for j in centers:
			z = np.array(i) - np.array(j)
			value = (-1) * gamma * np.dot(z, z)
			temp.append(math.exp(value))
		matrix.append(temp)
	phi = np.array(matrix)
	return np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi)), phi.T), Y)

def regularRBF(Xtrain, Ytrain, Xtest, Ytest, gamma, K):
	meanCalculator = KMeans(n_clusters=K, n_init=1, tol=0.0001)
	meanCalculator.fit(Xtrain)
	centers = meanCalculator.cluster_centers_
	w = getw(Xtrain, Ytrain, centers, gamma, K)

	XtoUseTemp = []
	for i in Xtest:
		temp = []
		temp.append(1)
		for j in centers:
			z = np.array(i) - np.array(j)
			value = (-1) * gamma * np.dot(z, z)
			temp.append(math.exp(value))
		XtoUseTemp.append(temp)
	XtestToUse = np.array(XtoUseTemp)

	error = 0
	for i in range(Ytest.shape[0]):
		out = np.dot(w.T, XtestToUse[i])
		if out < 0:
			value = -1
		else:
			value = 1
		if value != Ytest[i]:
			error = error + 1
	return error/(Ytest.shape[0]*1.0)

def hardMarginSVMEout(Xtrain, Ytrain, Xtest, Ytest, gamma):
	clf = svm.SVC( kernel='rbf', gamma=gamma, C=1000)
   	clf.fit(Xtrain, Ytrain)

   	error = 0
   	for i in range(Ytest.shape[0]):
   		out = clf.predict(Xtest[i])
   		if out < 0:
   			value = -1
   		else:
   			value = 1
   		if value != Ytest[i]:
   			error = error + 1
   	eout = error/(Ytest.shape[0]*1.0) 

   	error = 0
   	for i in range(Ytrain.shape[0]):
   		out = clf.predict(Xtrain[i])
   		if out < 0:
   			value = -1
   		else:
   			value = 1
   		if value != Ytrain[i]:
   			error = error + 1
   	ein = error/(Ytrain.shape[0]*1.0) 
   	return [ein, eout]

def experiment2():
	runs = 1000
	n = 100
	K = 12
	gamma = 1.5
	count = 0
	totalCount = 0
	for i in range(runs):
		print "Run =", i
		[Xtrain, Ytrain] = generateTrainingPoints(n)
		[Xtest, Ytest] = generateTrainingPoints(n)
		eout1 = regularRBF(Xtrain, Ytrain, Xtest, Ytest, gamma, K)
		[ein2, eout2] = hardMarginSVMEout(Xtrain, Ytrain, Xtest, Ytest, gamma)
		if ein2 == 0:
			totalCount = totalCount + 1
			if eout2 < eout1:
				count = count + 1
	print count/(totalCount * 1.0)

def regularRBFEin(Xtrain, Ytrain, Xtest, Ytest, gamma, K):
	meanCalculator = KMeans(n_clusters=K, n_init=1, tol=0.0001)
	meanCalculator.fit(Xtrain)
	centers = meanCalculator.cluster_centers_
	w = getw(Xtrain, Ytrain, centers, gamma, K)

	XtoUseTemp = []
	for i in Xtest:
		temp = []
		temp.append(1)
		for j in centers:
			z = np.array(i) - np.array(j)
			value = (-1) * gamma * np.dot(z, z)
			temp.append(math.exp(value))
		XtoUseTemp.append(temp)
	XtestToUse = np.array(XtoUseTemp)

	XtoUseTemp = []
	for i in Xtrain:
		temp = []
		temp.append(1)
		for j in centers:
			z = np.array(i) - np.array(j)
			value = (-1) * gamma * np.dot(z, z)
			temp.append(math.exp(value))
		XtoUseTemp.append(temp)
	XtrainToUse = np.array(XtoUseTemp)

	error = 0
	for i in range(Ytrain.shape[0]):
		out = np.dot(w.T, XtrainToUse[i])
		if out < 0:
			value = -1
		else:
			value = 1
		if value != Ytrain[i]:
			error = error + 1
	ein = error/(Ytrain.shape[0]*1.0)

	error = 0
	for i in range(Ytest.shape[0]):
		out = np.dot(w.T, XtestToUse[i])
		if out < 0:
			value = -1
		else:
			value = 1
		if value != Ytest[i]:
			error = error + 1
	eout = error/(Ytest.shape[0]*1.0)
	return [ein, eout]

def experiment3():
	runs = 1000
	n = 100
	gamma = 1.5
	count = [0, 0, 0, 0]
	for i in range(runs):
		print "Run =", i
		[Xtrain, Ytrain] = generateTrainingPoints(n)
		[Xtest, Ytest] = generateTrainingPoints(n)
		[ein1, eout1] = regularRBFEin(Xtrain, Ytrain, Xtest, Ytest, gamma, 9)
		[ein2, eout2] =	regularRBFEin(Xtrain, Ytrain, Xtest, Ytest, gamma, 12)
		if ein1 > ein2:
			if eout1 > eout2:
				count[3] = count[3] + 1
			else:
				count[0] = count[0] + 1
		else:
			if eout1 > eout2:
				count[1] = count[1] + 1
			else:
				count[2] = count[2] + 1 
	print count

def experiment4():
	runs = 1000
	n = 100
	K = 9
	count = [0, 0, 0, 0]
	for i in range(runs):
		print "Run =", i
		[Xtrain, Ytrain] = generateTrainingPoints(n)
		[Xtest, Ytest] = generateTrainingPoints(n)
		[ein1, eout1] = regularRBFEin(Xtrain, Ytrain, Xtest, Ytest, 1.5, K)
		[ein2, eout2] =	regularRBFEin(Xtrain, Ytrain, Xtest, Ytest, 2, K)
		if ein1 > ein2:
			if eout1 > eout2:
				count[3] = count[3] + 1
			else:
				count[0] = count[0] + 1
		else:
			if eout1 > eout2:
				count[1] = count[1] + 1
			else:
				count[2] = count[2] + 1 
	print count

def experiment5():
	runs = 1000
	n = 100
	K = 9
	gamma = 0.5
	count = 0
	for i in range(runs):
		print "Run =", i
		[Xtrain, Ytrain] = generateTrainingPoints(n)
		[Xtest, Ytest] = generateTrainingPoints(n)
		[ein, eout] = regularRBFEin(Xtrain, Ytrain, Xtest, Ytest, gamma, K)
		if ein == 0:
			count = count + 1
	print count/(runs * 1.0)

experiment5()
		