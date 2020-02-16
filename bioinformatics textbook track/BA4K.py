# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:20:14 2018

@author: palan
"""

amino_acid_mass = {'G' : 57, 'A' : 71, 'S' : 87, 'P' : 97, 'V' : 99, 'T' : 101, 'C' : 103,
    'I' : 113, 'L' : 113, 'N' : 114, 'D' : 115, 'K' : 128, 'Q' : 128, 'E' : 129,'M' : 131,
    'H' : 137, 'F' : 147, 'R' : 156, 'Y' : 163, 'W' : 186}

AminoAcid = []
AminoAcidMass = []
for i, j in amino_acid_mass.items():
    AminoAcid.append(i)
    AminoAcidMass.append(j)

def LinearSpectrum(Peptide, AminoAcid, AminoAcidMass):
    PrefixMass =  [0,] * (len(Peptide) + 1)
    for i in range(len(Peptide)):
        for j in range(20):
            if AminoAcid[j] == Peptide[i]:
                PrefixMass[i+1] = PrefixMass[i] + AminoAcidMass[j]
    LinearSpectrum  = [0,]
    for i in range(len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            LinearSpectrum.append(PrefixMass[j]  - PrefixMass[i])
    LinearSpectrum.sort()
    return LinearSpectrum
    
    
#a = LinearSpectrum("NQEL", AminoAcid, AminoAcidMass)
#b = '0 99 113 114 128 227 257 299 355 356 370 371 484'
#c = map(int, b.split(' '))
#res = 0
#for i in a:
#    if i in c:
#        idx = c.index(i)
#        res +=1
#        c.pop(idx)
#return res

def LinearScore(Peptide, Spectrum):
    res = 0
    a = LinearSpectrum(Peptide, AminoAcid, AminoAcidMass)
    c = Spectrum
    for i in a:
        if i in c:
            idx = c.index(i)
            res +=1
            c.pop(idx)
    return res
    



fname = 'rosalind_ba4k.txt'
lines = list(l for l in open(fname))
a = lines[0].strip()
b = lines[1].strip()
c = map(int, b.split(' '))
print LinearScore(a, c)