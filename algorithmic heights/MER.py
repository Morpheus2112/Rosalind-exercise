# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:22:05 2017

@author: Memphis
"""
f = open('rosalind_mer.txt', 'r')
texts = f.readlines()
f.close()

a =  [int(i) for i in texts[1].strip('\n').split(' ')]
b =  [int(i) for i in texts[3].strip('\n').split(' ')]


c = []
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] > b[j]:
        c.append(b[j])
        j += 1
     
    elif a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(a[i])
        c.append(b[j])
        i += 1
        j += 1
if j < len(b):
    c = c+b[j:]
if i< len(a):
    c = c+a[i:]    
g = open('output_mer.txt', 'w')
for i in range(len(c)):
    g.write(str(c[i])+' ')
g.close()