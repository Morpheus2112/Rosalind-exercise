# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 08:35:53 2018

@author: Memphis
"""
with open('rosalind_ba1a.txt') as input_data:
    S = input_data.readline().strip()
    s = input_data.readline().strip()

length = len(s)

count = 0
for l in range(len(S)-len(s)+1):

    if S[l:l+length] == s:
        count += 1

print(count)