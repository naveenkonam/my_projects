#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:32:49 2020

@author: konam
"""

import numpy as np

a = np.arange(10)

b = np.array([np.arange(4),2*np.arange(4)])

print(b.shape)

print(b[:,:])