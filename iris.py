#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:22:12 2020

@author: konam
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

X = X_iris[:,:2]
y = y_iris

print(X.shape)


