#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:38:26 2020

@author: konam
"""

import math

def area_cir(r):
    return (math.pi*(r**2))

n = eval(input('Please enter the radius to claculate the area of circle: '))

A = area_cir(n)

print("The area of the cirle with radius {0} is {1}".format(n, A))
    