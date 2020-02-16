# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:32:27 2018

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
    

def LinearScore(Peptide, Spectrum):
    res = 0
    a = LinearSpectrum(Peptide, AminoAcid, AminoAcidMass)
    c = Spectrum[:]
    for i in a:
        if i in c:
            idx = c.index(i)
            res +=1
            c.pop(idx)
    return res

def Trim(Leaderboard, Spectrum, N, AminoAcid, AminoAcidMass):
    LinearScores = [0,] * len(Leaderboard)
    for j in range(len(Leaderboard)):
        Peptide = Leaderboard[j]

        LinearScores[j] = LinearScore(Peptide, Spectrum)

    Leaderboard = [x for _,x in sorted(zip(LinearScores, Leaderboard), reverse =True)]
    LinearScores = [x for x,_ in sorted(zip(LinearScores, Leaderboard), reverse =True)]
  
    for j in range(N,len(Leaderboard)):
        if LinearScores[j] < LinearScores[N-1]:
            Leaderboard[j]=''
    return Leaderboard
#
#a = 'LAST ALST TLLT TQAS'.split(' ')
#b = map(int,'0 71 87 101 113 158 184 188 259 271 372'.split(' '))
#c = int('2')


fname = 'rosalind_ba4l.txt'
lines = list(l for l in open(fname))
a = lines[0].strip().split(' ')
b = map(int, lines[1].strip().split(' '))
c = int(lines[2].strip())

print ' '.join(Trim(a,b,c, AminoAcid,AminoAcidMass))
    