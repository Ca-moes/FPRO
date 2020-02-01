# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:08:45 2018

@author: andre_4mxog39
"""


def local_minima(alist,n):
    n = n//2
    result = []
    tries = []
    for indice,number in enumerate(alist):
        if indice-n<0:
            tries = alist[:indice+n+1]
            if number == min(tries):
                result += [(number,indice)]
        else:
            tries = alist[indice-n:indice+n+1]
            if number == min(tries):
                result += [(number,indice)] 
    for j in range(1,n+1):
        for i in range(len(result)-j):
            if result[i][0] == result[i+1][0] and int(result[i][1])+j == int(result[i+1][1]):
                result.remove(result[i+1])
                break
    return result

print(local_minima([2, 1, 1, 1, 7, 3, 1], 5))