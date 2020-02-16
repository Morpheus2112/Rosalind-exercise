# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:31:28 2018

@author: Memphis
"""

with open('rosalind_ba4a.txt') as input_data:
    
    rna = input_data.readline().strip()

from Bio.Seq import Seq
my_seq = Seq(rna)
my_seq.translate
print(my_seq.translate())