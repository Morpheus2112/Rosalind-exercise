# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 23:52:18 2017

@author: Memphis
"""

f = open('rosalind_ini5.txt', 'r')
texts = f.readlines()
f.close()
g = open('output_ini5.txt', 'w')
for i in xrange(len(texts)):
    if i % 2 == 1:
        g.write(texts[i])
g.close()