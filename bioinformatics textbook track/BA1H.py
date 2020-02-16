# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 09:51:40 2018

@author: Memphis
"""

with open('rosalind_ba1h.txt') as input_data:
    pattern = input_data.readline().strip()
    text = input_data.readline().strip()
    n = int(input_data.readline().strip())


"""
this definition borrowed from the previous assignment.
"""
    
def HammingDistance(text1,text2):
    res = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            res += 1
    return res

with open("ba1h.txt", "w") as outfile:

    for i in range(len(text)-len(pattern)+1):
        if HammingDistance(pattern, text[i:i+len(pattern)]) <= n:
            outfile.write(str(i)+' '),