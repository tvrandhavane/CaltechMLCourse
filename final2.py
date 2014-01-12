'''
Created on Jan 11, 2013

@author: Tanmay
'''
import numpy as np
from sklearn import svm

def main():
	temp = []
	temp.append([1, 0])
	temp.append([0, 1])
	temp.append([0, -1])
	temp.append([-1, 0])
	temp.append([0, 2])
	temp.append([0, -2])
	temp.append([-2, 0])
	Xtrain = np.array(temp)

	temp = []
	temp.append(-1)
	temp.append(-1)
	temp.append(-1)
	temp.append(1)
	temp.append(1)
	temp.append(1)
	temp.append(1)
	YtrainToUse = np.array(temp)

	clf = svm.SVC( kernel='poly', coef0=1, degree=2, gamma=1.0)
   	clf.fit(Xtrain, YtrainToUse)
   	print clf.support_vectors_.shape[0]

main()