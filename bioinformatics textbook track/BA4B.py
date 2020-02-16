# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:44:56 2018

@author: Memphis
"""

with open('rosalind_ba4b.txt') as input_data:
    
    seq = input_data.readline().strip()
    pro = input_data.readline().strip()

from Bio.Seq import Seq

k = len(pro) * 3
res = list()
for i in range(len(seq)-k+1):
    temp = seq[i:i+k]
    if Seq(temp).translate(stop_symbol='') == Seq(pro) or Seq(temp).reverse_complement().translate(stop_symbol='')== Seq(pro):
        res.append(temp)

with open('ba4b.txt','w') as f:
    for i in res:
        f.write(i)
        f.write('\n')