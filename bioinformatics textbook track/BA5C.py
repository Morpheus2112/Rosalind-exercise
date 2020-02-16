# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:47:18 2018

@author: palan
"""
import numpy as np

def longest_common_subsequence(v, w, indel = 0, scoring = None, verbose = False, local = False):
    '''
    CODE CHALLENGE: solve the Longest Common Subsequence Problem.
    Input: Two strings v and w
    Output: A longest common subsequence of v and w. 
    (Note: more than one solution may exist, in which case you may output any one.)
    '''
    n = len(v)
    m = len(w)
    s = np.zeros(shape = (n+1,m+1), dtype = np.float)
    for i in range(n+1):
        s[i, 0] = -indel * i
    for j in range(m+1):
        s[0, j] = -indel * j
    backtrack = np.chararray(shape = (n,m))
    for i in range(n):
        for j in range(m):
            if (scoring is None):
                score = (1 if v[i] == w[j] else 0)
            else:
                score = scoring[ v[i] ][ w[j] ]
            s[i+1, j+1] = max(s[i, j+1] - indel, s[i+1, j] - indel,
                s[i, j] + score)
            if s[i+1, j+1] == s[i, j+1] - indel:
                    backtrack[i, j] = '|'
            elif s[i+1, j+1] == s[i+1, j] - indel:
                    backtrack[i, j] = '-'
            elif s[i+1, j+1] == s[i, j] + score:
                    backtrack[i, j] = '/' if v[i] == w[j] else '*'
            # if local alignement is requested,
            # allow free-taxi ride from the source e.g. min s = 0
            # thus ensure s[i+1, j+1] > 0
            if (local and s[i+1, j+1] < 0):
                s[i+1, j+1] = 0
                backtrack[i, j] = 'x'
    lcs = []
    valign = []
    walign = []
    
    if local:
        # if local alignement is requested,
        # allow free-taxi ride to the sink
        # thus ensure s[i, j] is maximum over the entire graph
        (i, j) = np.unravel_index(s.argmax(),s.shape)
    else:
        (i, j) = (n, m)

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
        elif backtrack[i, j] == 'x':
            # break when a free-taxi ride back to source is allowed
            break            
        else:
            lcs.append(w[j])
            walign.append(w[j])
            valign.append(v[i])
            j -= 1
            i -= 1
    if not local:
        while (i>=0):
            walign.append('-')
            valign.append(v[i])
            i -= 1
        while (j>=0):
            valign.append('-')
            walign.append(w[j])
            j -= 1
        
    lcs.reverse()
    valign.reverse()
    walign.reverse()
    lcs = ''.join(lcs)
    valign = ''.join(valign)
    walign = ''.join(walign)
    if verbose:
        return (smax,valign,walign)
    else:
        return lcs

assert len(longest_common_subsequence('AACCTTGG','ACACTGTGA')) == 6

#v = 'ATAGTCTGCGTCCACCAAGAACTCGCGATACGGCTTGGGTGAGAGAAGAAATTGTTGGACTGTCGTGGGTATAACATCCGGGTCGAGGCGAAGGTCCGCTAGTTATCCCCTGGCGTGGCTAAATAGCAATTTTGCAGAATGCCTTATCTATCTTCAGCCATGCGCTTAACTAAATATTTTCAGTATAGTGTTACTAACGAGGAAGTCAAGTGCGTCTAATTTATTGAATAGAACTACTAGTTTTCCCCATAACGCCTAACTTTTAGAATACGATCTCTTTAGGATTAGAGATTTGCCAGGGCACACCGGGGTTGAGAGGGAAGGGGTTTGTACCTCGTGCGGCCTCAGGGGGGCGGTGTTGTCAGAATCTATCCGCACCCGCAGACCTATATTCCTACGTGGCAAGCCTGCATTTGTTAGCTGGTCCGCCTCGCGCAGGCGTCCGTCGGACCAGTGTCGAGAGCCCAATGCATTAGCAGTTCTTTGCCGTTATGGTTCTAAATGAGAAAGCACGTAGCCTTCGAATCAGTTTCCCGATTACTGGCTCCTCGACATAAAAAATCTGTCTCGAGTAGCATTCTGACGATAGGTTAGGGTGCCTGGAGTGAATTTAGCTGCATAATACCTTTGCGACCGTAGAAGACCCGGCCTGGATAGTGATCACCGCTGCTCCCCCATCTGGTTTCCTAGCTAATTGGGTCAGTGACTCTCCTCTCACTTGGGTTCTTCTTCTACGGAATCTGCGAAACACTGCAATATGGACCACAGAGCTTAAAGTATAGAGTCGCGCCAGTCACCACTCTGGTGATCAGTGAAGGGAATGATCACTCCAAACTGAACTCGCCGGTTTTAGTCTTGGCGGCCTTGTACGCTCACGGGTGAAGTAAGTACTAG'
#w = 'TTTCGCCGGGGCCTACGACAACTACACCACTTTTATTTCTCCTTATTGAATCTATGTTATCTGCGATAACGAGCAAGGGCACGGTCCGGTAGAATAAACTGGATGCATTAGGCACCATATTGAATTCAGGTGGGTACCGGTGTCCCCTCGTCCGGCGGACTAGCGGATGGCGGACATCAAGGGGGCGCACTGCCCAAGGGAAACACTCCGGGCATGCACCTCGATCACAGGTGTCTCACTCGTCACAGGTCTGCAAGTACCACGACAATTTCCTTCTCCTGGTGGATTCTTAGGGAGGAGTCCACTATACATACTCGTATCAGACTACTCAGGCCACCTCCTTAGGCGAAGGATATTCACCGGTGTGCGTTTGCAGACCCGACTGACCGTCTATGCCAGCCCTCAGTTATGCAAAATTTTACGATTTCACTGTCTACGTGGCCGGACTGGCCTGAACGGCAAAAAGGCAAGAGGATGAGCGCATATATGGGGTCCAGTTACATCACCAAATTCTAGGGCATTACTAAGCTATGACTGGCTACAGGTGTTGCGGTACCTCCCAGTAGATATTTGAGCGGAAACCGTATGACTGCAAGTTCGGATTAAGAGCCGCCGACGCTATCAGGCGCAGCGACAAATCGGAACGCGTCAGACGAACCAGGAAGAACGGCTGCTAGCCTTTACAACCTGATCAGCCCGTTGAGCGAAATGAATTACGGCTCGGGGGCAACTCTGACAGACCTCAGGTTTAAGCCTAAAACGTAGGACCCTTGAGCTTTCGCGCTATCTCCTAGAAGAAGGGAACCAGTGTCGCCTGTACGTTGCTGTAACCGTTTTTTGTACACCACAAGTCAGCCTCGCCCTCATTTTACTATGTCGGTGGCT'
fname = 'rosalind_ba5c.txt'
lines = list(l.strip() for l in open(fname))
v = lines[0].strip()
w = lines[1].strip()
print longest_common_subsequence(v,w)