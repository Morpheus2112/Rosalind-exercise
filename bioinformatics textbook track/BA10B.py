# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 19:34:15 2018

@author: Memphis
"""

with open('rosalind_ba10b.txt') as input_data:
    
    hidden = input_data.readline().strip()
    input_data.readline()
    input_data.readline()
    input_data.readline()
    seq = input_data.readline().strip()
    input_data.readline()
    input_data.readline()
    input_data.readline()
    input_data.readline()
#    mat = input_data.readlines()
    mat = [i.strip().split('\t')[1:] for i in input_data.readlines()]

cor = {'x':0,"y":1,'z':2,'A':0,'B':1}

prob = 1

for i in range(len(seq)):
    prob = prob * float(mat[cor[seq[i]]][cor[hidden[i]]])

print(prob)
