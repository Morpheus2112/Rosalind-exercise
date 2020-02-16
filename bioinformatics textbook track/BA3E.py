# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:29:12 2018

@author: Memphis
"""

with open('rosalind_ba3e.txt') as input_data:
    dna =  [i.strip() for i in input_data.readlines()]
    
res = dict()
for i in dna:
    seq = i[:-1]
    if seq not in res:
        res[seq] = list()
    res[seq].append(i[1:])
            

with open('ba3e.txt','w') as f:
    for i in res:
        f.write(i+' -> '+','.join(res[i])+'\n')