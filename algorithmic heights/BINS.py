# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 00:36:38 2017

@author: Memphis
"""
#
#n = 5
#m = 6
#A = [10,20,30,40,50]
#list = [40,10,35,15,40,20]
f = open('rosalind_bins.txt', 'r')
texts = f.readlines()
f.close()
n = int(texts[0].strip('\n'))
m = int(texts[1].strip('\n'))
A = [int(i) for i in texts[2].strip('\n').split(' ')]
list = [int(i) for i in texts[3].strip('\n').split(' ')]


def bi_find(A,i):
    lower = 0
    upper = len(A)
    while lower < upper:
        x = (lower + upper) // 2
        val = A[x]
        if i == val:
            return x + 1
        elif i > val:
            if lower == x:
                return -1
            lower = x
        elif i < val:
            upper = x

for i in list:
    print bi_find(A,i),