# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:14:13 2018

@author: Memphis
"""

mass = {}
mass['G'] = 57
mass['A'] = 71
mass['S'] = 87
mass['P'] = 97
mass['V'] = 99
mass['T'] = 101
mass['C'] = 103
mass['I'] = 113
mass['L'] = 113
mass['N'] = 114
mass['D'] = 115
mass['K'] = 128
mass['Q'] = 128
mass['E'] = 129
mass['M'] = 131
mass['H'] = 137
mass['F'] = 147
mass['R'] = 156
mass['Y'] = 163
mass['W'] = 186

with open('rosalind_ba4c.txt') as input_data:
    
    peptide = input_data.readline().strip()
    
def proteinMass(pep):
	weight = 0
	for x in pep:
		weight += mass[x]
	return weight

spec = [0]
for x in range(1,len(peptide)):
	for i in range(len(peptide)):
		if i+x > len(peptide):
			y = i+x-len(peptide)
			spec.append(proteinMass(peptide[i:]+peptide[:y]))
		else:
			spec.append(proteinMass(peptide[i:i+x]))
spec.append(proteinMass(peptide))
spec.sort()

print(' '.join(map(str,spec)))