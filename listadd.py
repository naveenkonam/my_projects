#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:57:34 2020

@author: konam
"""

from numpy import array, dot

from scipy import linalg

x = array([[1,1],[1,2],[1,3],[1,4]])
y = array([[1],[2],[3],[4]])

n = linalg.inv(dot(x.T,x))

k = dot(x.T,x)

coef = dot(n,k)

print(coef)