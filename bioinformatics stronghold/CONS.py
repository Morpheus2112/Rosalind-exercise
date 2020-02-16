# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:39:40 2017

@author: Memphis
"""

'''
Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n
matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the
value found at the intersection of row i and column j.
Say that we have a collection of DNA strings, all having the same length
n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of
times that'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
A consensus string c is a string of length n formed from our collection by
taking the most common symbol at each position; the jth symbol of c therefore
corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol,
leading to multiple possible consensus strings.
A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T
A   5 1 0 0 5 5 0 0
C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6
Consensus	A T G C A A C T
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in
FASTA format.
Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''

import sys
sys.path.append('../')
import rosalind_utils
import operator
def cons():
    # read sequences
    recs = rosalind_utils.read_fasta("rosalind_cons.txt")
    seqs = [rec[1] for rec in recs]
    matrix = []
    for i in xrange(len(seqs[0])):
        d = {'A':0, 'C':0, 'G':0, 'T':0}
        for seq in seqs:
            d[seq[i]] += 1
        matrix.append(d)

    # print consensus
    consensus = ''.join(max(col.iteritems(), key=operator.itemgetter(1))[0]
                        for col in matrix)
    print consensus
    # print matrix
    print 'A:', ' '.join(str(col['A']) for col in matrix)
    print 'C:', ' '.join(str(col['C']) for col in matrix)
    print 'G:', ' '.join(str(col['G']) for col in matrix)
    print 'T:', ' '.join(str(col['T']) for col in matrix)

cons()