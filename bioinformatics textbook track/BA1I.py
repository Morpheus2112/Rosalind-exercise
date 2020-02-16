# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 10:10:02 2018

@author: Memphis
"""
import itertools
with open('rosalind_ba1i.txt') as input_data:
    text = input_data.readline().strip()
    k, n = map(int,input_data.readline().strip().split())


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

def patternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	return 4 * patternToNumber(pattern[0:-1]) + symbolToNumber(pattern[-1:])

def symbolToNumber(symbol):
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3

def numberToPattern(x, k):
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)

def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

def approximatePatternCount(text, pattern, d):
	count = 0
	for i in range(len(text) - len(pattern) +1):
		test = text[i:i+len(pattern)]
		if hammingDistance(test, pattern) <= d:
			count = count+1
	return count

def frequentWordsWithMismatches(text, k, d):
	frequentPatterns = []
	frequencyArray = [0] * 4**k
	close = [0] * 4**k
	for i in range(len(text)-k):
		neighborhood = neighbors(text[i:i+k],d)
		for x in neighborhood:
			close[patternToNumber(x)] = 1
	for i in range(4**k):
		if close[i] == 1:
			pattern = numberToPattern(i,k)
			frequencyArray[i] = approximatePatternCount(text, pattern, d)
	maxCount = max(frequencyArray)
	for i in range(4**k):
		if frequencyArray[i] == maxCount:
			frequentPatterns.append(numberToPattern(i,k))
	return frequentPatterns

#text = "ACAATCGCGACAATCGCGACTCATCACCCGTGGAGTCACTCATCACACAATCGCGACTCATCACCGAGAACCAACTCATCACACAATCGCGCGAGAACCACACAAGTTACAATCGCGACTCATCACCCGTGGAGTCCACAAGTTACAATCGCGCACAAGTTACAATCGCGCGAGAACCAACAATCGCGCACAAGTTACTCATCACCGAGAACCACGAGAACCACCGTGGAGTCACTCATCACCCGTGGAGTCACAATCGCGACAATCGCGACAATCGCGCACAAGTTCCGTGGAGTCCGAGAACCAACTCATCACCGAGAACCAACTCATCACACAATCGCGCACAAGTTCCGTGGAGTCCGAGAACCACGAGAACCACGAGAACCAACTCATCACACTCATCACCGAGAACCAACAATCGCGACAATCGCGCGAGAACCACGAGAACCAACTCATCACACAATCGCGACTCATCACCCGTGGAGTCACAATCGCGACAATCGCGCCGTGGAGTCCGAGAACCACGAGAACCAACAATCGCGACAATCGCGCACAAGTTACAATCGCGACAATCGCGACTCATCACCGAGAACCACCGTGGAGTCCACAAGTTCACAAGTTACTCATCACCGAGAACCACACAAGTTCACAAGTTACAATCGCGCACAAGTTACTCATCACCCGTGGAGTCCCGTGGAGTCACTCATCACCCGTGGAGTCACTCATCACCGAGAACCAACAATCGCGCGAGAACCACGAGAACCACGAGAACCAACAATCGCGCGAGAACCACCGTGGAGTCACAATCGCGACAATCGCGCGAGAACCACCGTGGAGTCACTCATCACCGAGAACCAACTCATCACCACAAGTTACTCATCACACTCATCACACTCATCACACAATCGCGCGAGAACCAACAATCGCGCACAAGTTACAATCGCG"
#k = 6
#d = 3

a = frequentWordsWithMismatches(text, k, n)
p = ""
for x in a:
	p += x + " "
print(p)