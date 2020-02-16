# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 14:08:10 2018

@author: Memphis
"""

with open('rosalind_ba1n.txt') as input_data:
    text = input_data.readline().strip()
    d = int(input_data.readline().strip())


def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham    

def immediateNeighbors(pattern):
	neighborhood = [pattern]
	for i in range(len(pattern)):
		symbol = pattern[i]
		if symbol != 'A':
			neighborhood.append(pattern[0:i] + 'A' + pattern[i+1:])
		if symbol != 'C':
			neighborhood.append(pattern[0:i] + 'C' + pattern[i+1:])
		if symbol != 'G':
			neighborhood.append(pattern[0:i] + 'G' + pattern[i+1:])
		if symbol != 'T':
			neighborhood.append(pattern[0:i] + 'T' + pattern[i+1:])
	return neighborhood

def neighbors(pattern, d):
	if d == 0:
		return [pattern]
	if len(pattern) == 1:
		return ['A', 'C', 'G', 'T']
	neighborhood = []
	sufneigh = neighbors(pattern[1:],d)
	for x in sufneigh:
		if hammingDistance(pattern[1:],x) < d:
			for y in ['A', 'C', 'G', 'T']:
				 neighborhood.append(y + x)
		else:
			neighborhood.append(pattern[0] + x)
	return neighborhood

a =  neighbors(text, d )
with open('output_ms.txt','w') as g:
    for i in a:
        g.write(i+'\n')