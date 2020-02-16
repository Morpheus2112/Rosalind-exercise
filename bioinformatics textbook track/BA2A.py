# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 15:44:18 2018

@author: Memphis
"""

with open('rosalind_ba2a.txt') as input_data:
    k,d = map(int, input_data.readline().strip().split())
    seqs = [i.strip() for i in input_data.readlines()]
    
    
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


def trans(str):
    a = str.replace('A','0')
    b = a.replace('C','1')
    c = b.replace('G','2')
    d = c.replace('T','3')
#    print d
    num = int(d,4)
    
    return num

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


def MotifEnumeration(Dna, k,d):
    patterns = [0] * 4**k
    for x in Dna:
        for i in range(len(x)-k+1):
            neighborhood = neighbors(x[i:i+k],d)
            for n in neighborhood:
                inAll = True
                for y in Dna:
                    inY = False
                    for j in range(len(y)-k+1):
                        if hammingDistance(n,y[j:j+k]) <= d:
                            inY = True
                    if not inY:
                        inAll = False
                if inAll:
                    patterns[trans(n)] = 1
    finalPatterns = []
    for i in range(4**k):
        if patterns[i] == 1:
            finalPatterns.append(rev_trans(i,k))
    return finalPatterns


print(' '.join(MotifEnumeration(seqs, k,d)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    