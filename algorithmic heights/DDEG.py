# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 22:48:13 2017

@author: Memphis
"""

f = open('rosalind_ddeg.txt', 'r')
texts = f.readlines()
f.close()
n = int(texts[0].strip('\n').split(' ')[0])
m = int(texts[0].strip('\n').split(' ')[1])
edges = texts[1:]


b = dict()
for i in range(1,n+1):
    b[i] = []
for text in edges:
    a1, a2 =  text.strip('\n').split(' ')
    a1 = int(a1)
    a2 = int(a2)
    b[a1].append(a2)
    b[a2].append(a1)

for i in sorted(b.iterkeys()):
    sum = 0
    for j in b[i]:
        sum = sum + len(b[j])
    print sum