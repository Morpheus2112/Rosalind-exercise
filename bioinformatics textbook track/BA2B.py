# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 16:01:37 2018

@author: Memphis
"""

with open('rosalind_ba2b.txt') as input_data:
    k = int(input_data.readline().strip())
    seqs = [i.strip() for i in input_data.readlines()]
    
def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham

def rev_trans(index, k):
    st = ''
    for i in range(k):
        rem = index % 4
        st = str(rem)+ st
        index = index // 4
    
    a = st.replace('0','A')
    b = a.replace('1','C')
    c = b.replace('2','G')
    d = c.replace('3','T')
    return d

def disPatternText(Pattern, Texts):
    k = len(Pattern)
    distance = 0
    for x in Texts:
        hamming = k + 1
        for i in range(len(x)-k+1):
            z = hammingDistance(Pattern, x[i:i+k])
            if hamming > z:
                hamming = z
        distance += hamming
    return distance

def medianString(dna,k):
    distance = (k+1) * len(dna)
    median = ''
    for i in range(4**k):
        pattern = rev_trans(i,k)
        z = disPatternText(pattern, dna)
        if distance > z:
            distance = z
            median = pattern
    return median


print(medianString(seqs,k))

