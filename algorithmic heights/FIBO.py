# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 00:20:01 2017

@author: Memphis
"""


f = open('rosalind_fibo.txt', 'r')
texts = f.readlines()
f.close()

num = int(texts[0].strip('\n'))


def Fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    L = [0,] * (a+1)
    L[0] = 0
    L[1] = 1
    for i in xrange(2,a+1):
        L[i] = L[i-1] + L[i-2]
    return L[a]
    

print Fibo(num)