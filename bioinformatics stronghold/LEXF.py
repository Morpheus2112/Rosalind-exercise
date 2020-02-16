# -*- coding: utf-8 -*- 

"""
Problem
Assume that an alphabet A has a predetermined order; that is, we write the
alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the
English alphabet is organized as (A,B,…,Z).
Given two strings s and t having the same length n, we say that s precedes t in
the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't
match t[j] satisfies sj<tj in A.
Given: A collection of at most 10 symbols defining an ordered alphabet, and a
positive integer n (n≤10).
Return: All strings of length n that can be formed from the alphabet, ordered
lexicographically.
Sample Dataset
T A G C
2
Sample Output
TT
TA
TG
TC
AT
AA
AG
AC
GT
GA
GG
GC
CT
CA
CG
CCProblem
Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).
Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
Sample Dataset
T A G C
2
Sample Output
TT
TA
TG
TC
AT
AA
AG
AC
GT
GA
GG
GC
CT
CA
CG
CC
"""

import sys
sys.path.append('../')
import rosalind_utils
import itertools

def lexf():
    lines = open("rosalind_lexf.txt").readlines()
    lets = lines[0].split()
    n = int(lines[1])
    for x in itertools.product(lets, repeat=n):
        print ''.join(x)

lexf()