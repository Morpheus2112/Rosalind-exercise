# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:39:51 2017

@author: Memphis
"""


f = open('rosalind_ins.txt', 'r')
texts = f.readlines()
f.close()

n = int(texts[0].strip('\n'))
list = [int(i) for i in texts[1].strip('\n').split(' ')]

count = 0
for i in range(1,len(list)):
    k = i
    while k>0 and list[k] < list[k-1]:
        list[k-1], list[k] = list[k], list[k-1]
        count += 1
        k = k-1

print count