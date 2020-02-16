# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:42:01 2018

@author: Memphis
"""

with open('rosalind_ba2g.txt') as input_data:
    k, t ,n= map(int,input_data.readline().strip().split(' '))
    dna = [i.strip() for i in input_data.readlines()]
    
    
import random

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

def profileProbable(text, k, profile):
	maxprob = 0
	kmer = text[0:k]
	for i in range(0,len(text) - k +1):
		prob = 1
		pattern = text[i:i+k]
		for j in range(k):
			l = symbolToNumber(pattern[j])
			prob *= profile[l][j]
		if prob > maxprob:
			maxprob = prob
			kmer = pattern
	return kmer

def profileRandom(k, profile, text):
    probs = []
    for i in range(0,len(text) - k +1):
        prob = 1.0
        pattern = text[i:i+k]
        for j in range(k):
            l = symbolToNumber(pattern[j])
            prob *= profile[l][j]
        probs.append(prob)
    r = myRandom(probs)
    return r

def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham

def distanceBetweenPatternAndString(pattern, dna):
	k = len(pattern)
	distance = 0
	for x in dna:
		hamming = k+1
		for i in range(len(x) - k + 1):
			z = hammingDistance(pattern, x[i:i+k])
			if hamming > z:
				hamming = z
		distance += hamming
	return distance

def profileForm(motifs):
	k = len(motifs[0])
	profile = [[1 for i in range(k)] for j in range(4)]
	for x in motifs:
		for i in range(len(x)):
			j = symbolToNumber(x[i])
			profile[j][i] += 1
	for x in profile:
		for i in range(len(x)):
			x[i] = x[i]/len(motifs)
	return profile

def consensus(profile):
	str = ""
	for i in range(len(profile[0])):
		max = 0
		loc = 0
		for j in range(4):
			if profile[j][i] > max:
				loc = j
				max = profile[j][i]
		str+=numberToSymbol(loc)
	return str

def score(motifs):
	profile = profileForm(motifs)
	cons = consensus(profile)
	score = 0
	for x in motifs:
		for i in range(len(x)):
			if cons[i] != x[i]:
				score += 1
	return score

def myRandom(dist):
    s = 0.0
    for x in dist:
        s+= x
    i = random.random()
    partial = 0.0
    for x in range(len(dist)):
        partial += dist[x]
        if partial/s >= i:
            return x

def gibbsSampler(dna, k, t, n):
    bestMotifs = []
    motifs = []
    for x in range(t):
        i = random.randint(0, len(dna[x])-k)
        motifs.append(dna[x][i:i+k])
    bestMotifs = motifs[:]
    for i in range(n):
        j = random.randint(0,t-1)
        profile = profileForm(motifs[:j] + motifs[j+1:])
        r = profileRandom(k, profile, dna[j])
        motifs[j] = dna[j][r:r+k]
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs[:]
    return bestMotifs


best = gibbsSampler(dna, k, t, n)
s = score(best)
print(s)
for x in range(20):
    sample = gibbsSampler(dna, k, t, n)
    print(score(sample))
    if score(sample) < s:
        s = score(sample)
        best = sample[:]
for b in best:
	print(b)