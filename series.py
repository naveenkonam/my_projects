#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:05:18 2020

@author: konam
"""

import numpy as np
import pandas as pd

features = {'limbs':[0,4,4,4,8],'herbivore':['No','No','Yes','Yes','No']}

animals = ['Python','Iberian Lynx',\
           'Giant Panda','Field Mouse', 'Octopus']

df = pd.DataFrame(features, index = animals)

df['class'] = ['reptile','mammal','mammal','mammal','mollusc']

print(df)

grouped = df['class'].groupby(df['herbivore'])

print(grouped.groups)
grouped.size