# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 09:06:07 2018

@author: Memphis
"""


with open('rosalind_ba1d.txt') as input_data:
    pattern = input_data.readline().strip()
    seq = input_data.readline().strip()

i = 0
index = 0
while (index !=-1):
    try:
        index =  seq.index(pattern, i)
        i = index +1
        print(index),
    except ValueError:
        index = -1
    