# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:35:57 2018

@author: navi_
"""

from sklearn.naive_bayes import MultinomialNB
import numpy as np
from pprint import pprint

X = np.random.randint(5, size=(6,100))
y = np.array([1,2,3,4,5,6])

clf = MultinomialNB()
clf.fit(X, y)

pprint(X)
print(clf.predict(X[2:3]))