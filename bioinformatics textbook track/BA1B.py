# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 08:44:27 2018

@author: Memphis
"""

with open('rosalind_ba1b.txt') as input_data:
    text = input_data.readline().strip()
    k = int(input_data.readline().strip())
kmers = {}

for i in range(len(text)-k+1):
	pattern = text[i:i+k]
	if pattern in kmers.keys():
		kmers[pattern] += 1
	else:
		kmers[pattern] = 1

printMax = ""
max = 0
for p,v in kmers.items():
    if v > max:
        printMax = p
        max = v
    else:
        if v == max:
            printMax += " " + p

print(printMax)