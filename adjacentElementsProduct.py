#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 07:38:43 2020

@author: Jack Kim
"""

"""
Problem:
    For inputArray = [3, 6, -2, -5, 7, 3], the output should be
    adjacentElementsProduct(inputArray) = 21.
    
    7 and 3 produce the largest product.
"""

def adjacentElementsProduct(inputArray):
    largest=-1000
    for i in range(len(inputArray) - 1 ):
        if largest < (inputArray[i] * inputArray[i+1]):
            largest=inputArray[i] * inputArray[i+1]
    return largest
        
inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray))    