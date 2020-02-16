# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 08:49:19 2018

@author: Memphis
"""

with open('rosalind_ba3a.txt') as input_data:
    k = int(input_data.readline().strip())
    text = input_data.readline().strip()
    
a = set()
for i in range(len(text)-k+1):
    a.add(text[i:i+k])

with open('ba3a.txt','w') as f:
    for i in a:
        f.write(i)
        f.write('\n')