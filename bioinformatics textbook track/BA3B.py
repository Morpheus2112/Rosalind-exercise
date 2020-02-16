# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 08:57:11 2018

@author: Memphis
"""

with open('rosalind_ba3b.txt') as input_data:
    texts =  [i.strip() for i in input_data.readlines()]

st = texts[0]
for i in range(1,len(texts)):
    st = st + texts[i][-1]

print(st)