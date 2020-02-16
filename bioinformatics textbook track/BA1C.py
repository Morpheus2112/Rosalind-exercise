# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 09:01:11 2018

@author: Memphis
"""

from Bio.Seq import Seq

with open('rosalind_ba1c.txt') as input_data:
    pattern = input_data.readline().strip()

my_seq = Seq(pattern)


print(my_seq.reverse_complement())