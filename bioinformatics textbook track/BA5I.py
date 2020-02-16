# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:57:48 2018

@author: palan
"""
import numpy as np

def overlap_alignement(v, w):
    '''
    CODE CHALLENGE: 
    Solve the Overlap Alignment Problem.
    Input: Two strings v and w, each of length at most 1000.
    Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of
    v and a prefix w' of w achieving this maximum score. Use an alignment score in which matches count
    +1 and both the mismatch and indel penalties are 2.    
    '''
    n = len(v)
    m = len(w)
    indel = 2
    s = np.zeros(shape = (n+1,m+1), dtype = np.float)
    for i in range(n+1):
        # free-ride taxi from source on v to take account 
        # of the overlap-alignement-nature for a prefix-source
        s[i, 0] = 0
    for j in range(m+1):
        s[0, j] = -indel * j
    backtrack = np.chararray(shape = (n,m))
    for i in range(n):
        for j in range(m):
            score = (1 if v[i] == w[j] else -indel)
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
    
    # for overlap alignement 
    # allow free-taxi ride from the end of source to the sink on v
    # thus ensure s[i, j] is maximum over the last row of graph
    i = n
    j = s[n,:].argmax()

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
    
assert overlap_alignement('PAWHEAE', 'HEAGAWGHEE')[0] == 1.0

fname = 'rosalind_ba5i.txt'
lines = list(l.strip() for l in open(fname))
v = lines[0].strip()
w = lines[1].strip()
#v = 'GCTATAAGAATAAACCACTAGATCACCTCCGGCTCGCTCACTCCTGATCATGGTTCGTGCTAACATCGCGCCGCGCTGACGCCGAATCGTTCGTAGGAGACAAGTCGACGACCTCATCTACAGGCAAAAGTTAAATTAGCTCTCGGCTAGATGTGACAATCGGAACCCTGCACCCTGCGTAATAGGGTAAATAGTCGGGAGTTGATGCACACACCTAGATATTGGCTGAATGACAGACTGCCATTCCTGCACTGGAAAGTAGAGTGCATATGTTTCGTGAGATTATGCAGGCTCTACGGTTATACTGGGCTCCACGGATTCGACCGGTACTGTTGATTGAAGACTCTTCTATAGAGGCTCTAACCGCGGAGGCCGCAACCAATCGACAATGAAGCACCCGTCGTCGGTATCGTTGGGAAGGACGACACCGTAAGGGCAGACTTTATCGTGACCCGTCTGCTTGCTAGAAAAGCCCTGGCGTTTGTACAACGTCCGTGCAGAATTAGCGTTTTTCTCAGGAAAGATGAGGGGGTTGATCATCATCTCGTTTCGCACGGGTCAAGCGCATTTTCCTACTGTTTTGGACACAGTACGTCTTCCACTGATCTCATACGGACATTACCAGCACCCTTTTGTACCTGTCGTAACTTGTGCCATTCTAGGCCCGTTTTCACTTGCGCTTATGATCATGGTTCCGCTGATCTATATGGGCCGGGTAGGGCACTCCCAGATGAAGGGGAGTAATGGTAGCCGGATCCAAGTGACGCGCCCTAGCGGCTCCGGAGTTTGATAGACGTCGTGCTATGGAGCGTTGGAGCGACAACGCGCTCGTGCTCTGGAAGGTCGCTGCTGATCCGTAA'
#w = 'TACTGGTCCTGACCCACCTCACTTTGATGTCCCCTTTTCTCGTTTGCGCATCAAGATCTGGCCCGCAACTATTGGCCGTGAAAGGCACTCATCAATAAAGACAGTACTCACGCGGTCGGATCCAAATGCGCGCACCGAGCGGCCCAGGAGTTGATAGCGTCGAGTAACCTATTAGGACTCGAGGCAACTCGCGCTCTCTCAGGAGGCTCGCCTGCTAGTCCGTGAACGACGGATCTTTGGTGCTGCCTTCCTATCATGACATTGCCTAATAACGAGCGGCACCTACTCCCAGGTCTTTGAAGGGATGGCTTGTTTACCCCGATTCCGAGAAATAGAGATGACTCCTAAGGAAGTAATGAAGGAAGTTCAGTGGTATGGGTATCGTTTAGTTTGCCAGGGAGATTGCCCATAACCTAAGTCCCTAATACAGCAGTAGATCTCACCATAGATGTAGGAAAGCACAGTGATTTAGACGCTTAGCCAAATACAAAGGAATGTACCCCCTCCTAACACTGAGCACCGCTTATTTACTAGTATACTCAGAGTGTGGAGCGCTGAACGTTGTGTCAACAAGAACATAAGCCGCCGTGAATGAATTTGTGAAGGGGAGTGATCATGGTTTTACTCGTGGTAGATTTGGGCAGAACCTGATTCCTCACGTGTGAATGTAATTGAAGCTGACTCCCACACATACAGGCACGATTCTTTTAGATGATGTTTTAGGAAGCGCATTTCGTATTAACACTGCCTTGCATTTGATAACCATCACTTGTTCATTACATGATCCCATAGGGCCGTGTTGTTACTTTCGTGTTAGTCGAGCAGTATGACCACCTTTTCGGCGCTTGATATGCCTCAAGACGTGCGATTCAAGGAATCAAACAAATGAACGCCGCACTGGATGACTGGG'
(a,b,c) = overlap_alignement(v, w)
print int(a)
print b
print c