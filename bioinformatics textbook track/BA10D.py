# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 21:04:15 2018

@author: Memphis
"""

import numpy as np

with open("rosalind_ba10d.txt") as infile:
    observations = infile.readline().strip()
    infile.readline() # separating line
    alphabet = dict((char, index) for index, char in enumerate(infile.readline().strip().split()))
    infile.readline() # separating line
    states = dict((state, index) for index, state in enumerate(infile.readline().strip().split()))

    infile.readline() # separating linesAAAAAAABAAABABAAABABAABABAABBAABBAAAABABAAAAABAAAAAABABABABABABBAAAAABBAABAAAABABAABAABBAAAAABAAAAB
    infile.readline() # separating lines

    t = np.zeros( (len(states), len(states)))
    for row in range(len(states)):
        line = infile.readline()
#        print(line)
        for col, prob in enumerate(line.split()[1:]):
            t[row][col] = prob
#            print(prob)

    infile.readline() # separating lines
    infile.readline() # separating lines

    e = np.zeros( (len(states), len(alphabet)));
    for row, line in enumerate(infile.readlines()):
        for col, prob in enumerate(line.split()[1:]):
            e[row][col] = prob

c = np.zeros( len(observations) ) # to scale factors

	# build trellis
V = [{st :  (1.0 / len(states)) * e[states[st]][alphabet[observations[0]]] for st in states}]
#	c[0] = 1.0 / sum(V[0][st]["prob"] for st in states)
#	for st in states:
#		V[0][st]["prob"] *= c[0] # normalize

for i in range(1, len(observations)):
    V.append({})
    for this in states:
        V[i][this] = 0
        for last in states:
            V[i][this] += V[i-1][last]*t[states[last]][states[this]]*e[states[this]][alphabet[observations[i]]]
     
res = 0
for i in states:
    res += V[-1][i]

print(res)