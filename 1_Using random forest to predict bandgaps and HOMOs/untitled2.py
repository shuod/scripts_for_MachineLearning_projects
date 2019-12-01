# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:18:20 2019

@author: Odysseus
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import pickle

#方法一:python自带的pickle
(X,y) = datasets.load_iris(return_X_y=True)
rfc = RandomForestClassifier(n_estimators=100,max_depth=100)
rfc.fit(X,y)
print(rfc.predict(X[0:1,:]))


#save model
f = open('rfc.pickle','wb')
pickle.dump(rfc,f)
f.close()


#load model
f = open('rfc.pickle','rb')
rfc1 = pickle.load(f)
f.close()
print(rfc1.predict(X[0:1,:]))