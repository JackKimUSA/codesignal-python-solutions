#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 07:31:59 2020

@author: Jack Kim
"""

"""
Problem:
    Given the string, check if it is a palindrome.
"""

def checkPalindrome(inputString):
    if inputString == inputString[-1::-1]:
        return True
    else:
        return False
    
print(checkPalindrome("aabaa"))

