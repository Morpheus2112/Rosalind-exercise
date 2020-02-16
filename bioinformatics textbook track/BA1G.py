# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 09:48:11 2018

@author: Memphis
"""

with open('rosalind_ba1g.txt') as input_data:
    text1 = input_data.readline().strip()
    text2 = input_data.readline().strip()

res = 0
for i in range(len(text1)):
    if text1[i] != text2[i]:
        res += 1
print(res)