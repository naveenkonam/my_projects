#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:24:15 2020

@author: konam
"""

def main():
    '''Print the squres of the numbers from 0 to n'''
    
    n = input("Please enter a number: ")
    '''x = range(int(n)+1)'''
    y= [sq**2 for sq in range(int(n)+1)]
    
    print(y)
    
main()
    