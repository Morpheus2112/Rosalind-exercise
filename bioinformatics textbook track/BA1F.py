# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 09:39:59 2018

@author: Memphis
"""
#
with open('rosalind_ba1f.txt') as input_data:
    text = input_data.readline().strip()
res = [0]* (len(text)+1)
for i in range(len(text)):
    if text[i] == 'C':
        res[i+1] = res[i] - 1
    elif text[i] == "G":
        res[i+1] = res[i] +  1
    else:
        res[i+1] = res[i]
value =  min(res)
for i in range(1,len(res)):
    if res[i] == value:
        print(i),
    