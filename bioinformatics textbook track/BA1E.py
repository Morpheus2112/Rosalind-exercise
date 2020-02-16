# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 09:15:32 2018

@author: Memphis
"""

with open('rosalind_ba1e.txt') as input_data:
    text = input_data.readline().strip()
    k, L, t = map(int, input_data.readline().strip().split())
    
kmers = {}
for i in range(len(text)-k+1):
	pattern = text[i:i+k]
	if pattern in kmers.keys():
		kmers[pattern] += 1
	else:
		kmers[pattern] = 1
#print len(kmers)
"""
delete all the kmers with less than t repeats in whole length
will decrease the search space in later search

very clever!
"""
kmers2 = kmers.copy()
for i in kmers2:
    if kmers2[i] < t:
        del kmers[i]
#print len(kmers)
res = []
for i in range(len(text) - L + 1):
    for pattern in kmers.keys():
        if text[i:i+L].count(pattern) >= t:
            if pattern not in res:
                res.append(pattern)

print(' '.join(res))