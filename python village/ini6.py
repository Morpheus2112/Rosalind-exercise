# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 00:01:56 2017

@author: Memphis
"""
f = open('rosalind_ini6.txt', 'r')
text = f.readline()
f.close()
b = dict()
for word in text.split(' '):
    if b.has_key(word):
        b[word] += 1
    else:
        b[word] = 1

for i ,j in b.items():
    print i + ' ' + str(j)