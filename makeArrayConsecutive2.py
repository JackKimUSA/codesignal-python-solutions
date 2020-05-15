#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 07:59:36 2020

@author: Jack Kim
"""

"""
Problem:
    Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
    each statue having an non-negative integer size. Since he likes to make things perfect, 
    he wants to arrange them from smallest to largest so that 
    each statue will be bigger than the previous one exactly by 1. 
    He may need some additional statues to be able to accomplish that. 
    Help him figure out the minimum number of additional statues needed.
"""

def makeArrayConsecutive2(statues):
    total=0
    statues.sort()
    start=statues[0]
    for i in range(1, len(statues)):
        while (start + 1) != statues[i]:
            total += 1
            start += 1
        start += 1
    return total
            


statues = [6, 2, 3, 8]
print(makeArrayConsecutive2(statues))