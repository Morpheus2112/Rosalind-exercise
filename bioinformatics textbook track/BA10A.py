# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:42:11 2018

@author: Memphis
"""

with open('rosalind_ba10a.txt') as input_data:
    
    seq = input_data.readline().strip()
    input_data.readline()
    input_data.readline()
    input_data.readline()
    input_data.readline()
    mat = [i.strip().split('\t')[1:] for i in input_data.readlines()]
    
prob = 0.5
cor = {'A':0,"B":1}
for i in range(len(seq)-1):
    prob = prob * float(mat[cor[seq[i]]][cor[seq[i+1]]])

print(prob)