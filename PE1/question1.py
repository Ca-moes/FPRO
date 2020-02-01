#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:10:49 2018

@author: exame
"""
# In an Armstrong number of 3 digits, the sum of the cubes of each
# digit is equal to the number itself

num = int(input("What's the number: "))
dig3 = num % 10 
dig2 = (num//10) % 10
dig1 = (num//100) % 10

ntest = dig1**3 + dig2**3 + dig3**3 
result= (ntest == num)
print(result)
