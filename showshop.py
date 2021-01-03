#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:10:15 2020

@author: konam
"""

from collections import Counter

No_Shoes = eval(input("Enter no of shoes: "))
Shoe_sizes = input("Enter show sizes available: ")

C = Counter(Shoe_sizes)

No_Purchase = eval(input("Enter no of Purchases: "))
item_purchase = []
for no in range(1,No_Purchase+1):
    item_purchase.append(input("Enter shoe size and price with a space: "))

print(item_purchase)
print(C)