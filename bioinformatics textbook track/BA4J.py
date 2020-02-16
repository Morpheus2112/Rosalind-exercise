# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:03:38 2018

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
    return LinearSpectrum
    
    
a = LinearSpectrum("QGHGGHEKTAEVSTEFCGAFQDYITVDMMFVDCYPCTLSTE", AminoAcid, AminoAcidMass)
a.sort()
print ' '.join(map(str,a))