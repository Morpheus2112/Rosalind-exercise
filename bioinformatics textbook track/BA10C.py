# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 19:45:38 2018

@author: Memphis
"""

#with open('rosalind_ba10c.txt') as input_data:
#    
#    hidden = input_data.readline().strip()
#    input_data.readline()
#    input_data.readline()
#    input_data.readline()
#    input_data.readline()
#    input_data.readline()
#    input_data.readline()
#    a = input_data.readline()
#    b = input_data.readline()
#    trans =  [i.strip().split('\t')[1:] for i in [a,b]]    
#    input_data.readline()
#    input_data.readline()
##    mat = input_data.readlines()
#    emit = [i.strip().split('\t')[1:] for i in input_data.readlines()]
#    
#cor = {'x':0,"y":1,'z':2,'A':0,'B':1}
#
#A = [0] * len(hidden)
#B = [0] * len(hidden)
#A[0] =  float(emit[0][cor[hidden[0]]])
#B[0] =  float(emit[1][cor[hidden[0]]])
#pre = max(A[0],B[0])
#seq = 'A' if A[0] > B[0] else 'B'


import numpy as np
import operator
import pdb

with open("rosalind_ba10c.txt") as infile, open("ba10c.txt", "w") as outfile:
	observations = infile.readline().strip()
	infile.readline() # separating line
	alphabet = dict((char, index) for index, char in enumerate(infile.readline().strip().split()))
	infile.readline() # separating line
	states = dict((state, index) for index, state in enumerate(infile.readline().strip().split()))

	infile.readline() # separating lines
	infile.readline() # separating lines

	t = np.zeros( (len(states), len(states)))
	for row in range(len(states)):
		line = infile.readline()
		for col, prob in enumerate(line.split()[1:]):
			t[row][col] = prob

	infile.readline() # separating lines
	infile.readline() # separating lines

	e = np.zeros( (len(states), len(alphabet)));
	for row, line in enumerate(infile.readlines()):
		for col, prob in enumerate(line.split()[1:]):
			e[row][col] = prob

	c = np.zeros( len(observations) ) # to scale factors

	# build trellis
	V = [{st : {"prob" : (1.0 / len(states)) * e[states[st]][alphabet[observations[0]]], "prev" : None} for st in states}]
	c[0] = 1.0 / sum(V[0][st]["prob"] for st in states)
#	for st in states:
#		V[0][st]["prob"] *= c[0] # normalize

	for n in range(1, len(observations)):
		V.append({})
		for state in states:
			prob, prev_st = max(((V[n-1][prev_state]["prob"] * t[states[prev_state]][states[state]], prev_state) for prev_state in states), key = operator.itemgetter(0))
			V[n][state] = {"prob" : prob * e[states[state]][alphabet[observations[n]]], "prev" : prev_st}
		c[n] = 1.0 / sum(V[n][st]["prob"] for st in states)
#		for st in states:
#			V[n][st]["prob"] *= c[n] # normalize		

	# pdb.set_trace()
	for item in V:
		print(item)
	prev, state = max(((V[-1][st]["prev"], st) for st in V[-1]), key=lambda s: V[-1][s[1]]["prob"])
	path = state
	for i in range(len(V) - 2, -1, -1):
		path = prev + path
		prev = V[i][prev]["prev"]

	print(observations)
	print(states)
	print(t)
	print(e)
	print(path)

	outfile.write(path)