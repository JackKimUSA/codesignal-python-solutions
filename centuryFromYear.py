#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 07:12:17 2020

@author: Jack Kim
"""

"""
Problem:
    Given a year, return the century it is in. 
    The first century spans from the year 1 up to and including the year 100, 
    the second - from the year 101 up to and including the year 200, etc.
"""
def centuryFromYear(year):
    c=int(year/100)
    if year%100 == 0 :
        return c
    else:
        return c + 1
    
print(centuryFromYear(1700))
print(centuryFromYear(1988))
    

