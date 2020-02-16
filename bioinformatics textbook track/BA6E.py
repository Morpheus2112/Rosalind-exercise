# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:08:11 2018

@author: Memphis
"""

k = 3
a = 'AAACTCATC'
b = 'TTTCAAATC'

def shared_kmers(k,a,b):
    '''
    CODE CHALLENGE: Solve the Shared k-mers Problem.
    Shared k-mers Problem: Given two strings, find all their shared k-mers.
    Input: An integer k and two strings.
    Output: All k-mers shared by these strings, 
    in the form of ordered pairs (x, y).
    '''    
    def reverse_complement(pattern):
        rev = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        reverse = map(lambda c: rev[c], pattern[::-1])
        return ''.join(reverse)
    
    def kmers_dict(k, text):
        ''' 
        Solve the String Composition Problem.
        Input: An integer k and a string Text.
        Output: returns a k-mers:[positions,] dictionnary
        '''
        kmers = {}
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            kmers[kmer] = kmers.setdefault(kmer,[]) + [i]
            kmers[reverse_complement(kmer)] = kmers[kmer]
        return kmers
    
    shared = []
        
    bkmers = kmers_dict(k,b)
    for i in range(len(a) - k + 1):
        akmer = a[i:i+k]
        if akmer in bkmers:
            shared += [(i,j) for j in bkmers[akmer]]
    
    return sorted(shared)
        

fname = 'rosalind_ba6e.txt'
lines = list(l for l in open(fname))
k = int(lines[0])
a = lines[1].strip()
b = lines[2].strip()
with open(fname+'.out.txt', "w") as f:
        f.write('\n'.join(map(str,shared_kmers(k,a,b))))
