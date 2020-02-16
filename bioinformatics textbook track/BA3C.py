# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:06:41 2018

@author: Memphis
"""

with open('rosalind_ba3c.txt') as input_data:
    dna =  [i.strip() for i in input_data.readlines()]
    
adj = [[0 for x in range(len(dna))] for y in range(len(dna))]
for i in range(len(dna)):
	for j in range(len(dna)):
		if i!=j:
			if dna[i][1:] == dna[j][:-1]:
				adj[i][j] = 1


with open('ba3c.txt','w') as f:

    for i in range(len(adj)):
    	for j in range(len(adj[i])):
    		if adj[i][j] == 1:
    			f.write(dna[i] + " -> " + dna[j]+'\n')
