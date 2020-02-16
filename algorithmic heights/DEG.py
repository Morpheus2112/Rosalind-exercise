# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 01:20:27 2017

@author: Memphis
"""

f = open('rosalind_DEG.txt', 'r')
texts = f.readlines()
f.close()
n = [int(i) for i in texts[1].strip('\n').split(' ')][0]
edges = texts[1:]


b = dict()
for text in edges:
    for word in text.strip('\n').split(' '):
        if b.has_key(word):
            b[word] += 1
        else:
            b[word] = 1
for i in xrange(1,n+1):
    print b[str(i)],