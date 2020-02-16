# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:13:24 2018

@author: Memphis
"""

with open('rosalind_ba3d.txt') as input_data:
    k = int(input_data.readline().strip())
    text = input_data.readline().strip()

kn = k-1
res = dict()
for i in range(len(text)-kn):
    if text[i:i+kn] not in res:
        res[text[i:i+kn]]=set()
        res[text[i:i+kn]].add(text[i+1:i+kn+1])
    else:
        res[text[i:i+kn]].add(text[i+1:i+kn+1])

with open('ba3d.txt','w') as f:
    for i in res:
        f.write(i+' -> '+','.join((res[i]))+'\n')
    
    