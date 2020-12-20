#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:58:48 2020

@author: konam
"""

import numpy as np
import matplotlib.pyplot as plt

from pylab import *

x = np.linspace(-5,5,200)

y1 = x**2
y2 = x**3

fig,ax = plt.subplots()

ax.plot(x,y1,'r',label=r"$y_1 = x^2$",linewidth=2)
ax.plot(x,y2,'k--',label=r"$y_2 = x^3$",linewidth=4)

ax.legend(loc=2)

ax.set_xlabel(r'$x$',fontsize=18)
ax.set_ylabel(r'$y$',fontsize=18)

ax.set_title('My Figure')

plt.show
