# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:33:28 2018

@author: palan
"""
import numpy as np

def fitting_alignement(v, w):
    '''
    CODE CHALLENGE: 
    Solve the Fitting Alignment Problem.
    Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
    Output: A highest-scoring fitting alignment between v and w. Use the simple scoring method in which
    matches count +1 and both the mismatch and indel penalties are 1.    
    '''
    n = len(v)
    m = len(w)
    indel = 1
    assert n > m
    s = np.zeros(shape = (n+1,m+1), dtype = np.float)
    for i in range(n+1):
        # free-ride taxi from source on v to take account of the fitting alignement
        s[i, 0] = 0
    for j in range(m+1):
        s[0, j] = -indel * j
    backtrack = np.chararray(shape = (n,m))
    for i in range(n):
        for j in range(m):
            score = (1 if v[i] == w[j] else -1)
            s[i+1, j+1] = max(s[i, j+1] - indel, s[i+1, j] - indel,
                s[i, j] + score)
            if s[i+1, j+1] == s[i, j+1] - indel:
                    backtrack[i, j] = '|'
            elif s[i+1, j+1] == s[i+1, j] - indel:
                    backtrack[i, j] = '-'
            elif s[i+1, j+1] == s[i, j] + score:
                    backtrack[i, j] = '/' if v[i] == w[j] else '*'
    lcs = []
    valign = []
    walign = []
    
    # for fitting alignement 
    # allow free-taxi ride to the sink on v
    # thus ensure s[i, j] is maximum over the last column of graph
    i = s[:,m].argmax()
    j = m

    smax = s[i, j]
    
    i -= 1
    j -= 1

#    print '------------'
#    print s
#    print backtrack
#    print local,i,j
#    print '------------'
    
    while (i >= 0 and j >= 0):
#        assert backtrack[i,j] != '*'
        if backtrack[i, j] == '|':
            walign.append('-')
            valign.append(v[i])
            i -= 1
        elif backtrack[i, j] == '-':
            walign.append(w[j])
            valign.append('-')
            j -= 1           
        else:
            lcs.append(w[j])
            walign.append(w[j])
            valign.append(v[i])
            j -= 1
            i -= 1
        
    lcs.reverse()
    valign.reverse()
    walign.reverse()
    lcs = ''.join(lcs)
    valign = ''.join(valign)
    walign = ''.join(walign)
    return (smax,valign,walign)

assert fitting_alignement('GTAGGCTTAAGGTTA', 'TAGATA')[0] == 2.0

#v = 'ATCGCGACAACGGTACCACATCAGAGCCGATCTTTTAGAGATACTTCAGCTGCCAATGGGTCAGCCGTAGCGAACGAACTCTAACCTGTGGCGGGTGCTCGACGACGGAGGTAGTGAACAGTCGTGACTTGATCCAAGATGAATCTGGTTATGTTTCGCTATATCACGATAGGGATTGGTGTATTTAACGGGGGTTATGTGACAACAACCGTGGTTGCCACCATAGCCGAGGCTCGAGCGTACCAAGGCCGGATATATACGGTTTTCTTTTTCGCAGCTAGTCTAGAACAGTATCGTTCAGACCCTGCTAAGGCGCTCGCAGCTCGGGCATCCCACCGGTATTATCATGAAACTGAATGACCTACTTGTTAGGTCCCTTGAACGACTTGCTATTTAGCTAGTTTGAGGTTGCCGTAGTCCTCAAGTAAAATTTAAGGGTATGCGTGACGATTAGTCGGAAGTTCAGCTCGATATAACCGGTAATCCTCTCCCAGATACGAGAACTGGCGGGGGGTTGCAAGTATATGCTAGACGACAATTGGGGTGGACAATTGGTGGACTAGAACTCTCGGAATCGAGTCGCTTTACTTTGCGAGATTTTGTTACCACCTCGTAACATGTTCGATCAAATACAGGAAGCCGGGTCTCGCAAGCATTAGTTCCCTTTTCGGCAGTCTTTGGGTCAATTTATGTGGTTTCAGTAGCTGCGAGACGAGGCGCGGAACGTTCTTCACACGACACCGGCATCTTATGCAGACATACCTGAGATGACTCGCGGTTATAGAGTAAATGACACCAGCGGCCTATAGAAGGTGCCGGCGTGCTTC'
#w = 'TCAAATATCGGGTCGCACCCAGTCCGGAAGCGCTCCGACGACCCTTAGGTGTATGACGTGGAGAAGCTTCGACGCGTTGAGTCAAGATAA'

fname = 'rosalind_ba5h.txt'
lines = list(l.strip() for l in open(fname))
v = lines[0].strip()
w = lines[1].strip()


(a,b,c) = fitting_alignement(v, w)
print int(a)
print b
print c