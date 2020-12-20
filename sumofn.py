#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:35:13 2020

@author: konam
"""
sum1 = 0

for n in range(1000):
    if(n%3==0 or n%5==0):
        sum1 = sum1 + n
    else:
        pass
    
print(sum1)


s = [y for y in range(1000) if y%3==0 or y%5==0]

n = 0

for x in s:
    n = n + x
    
print(n)