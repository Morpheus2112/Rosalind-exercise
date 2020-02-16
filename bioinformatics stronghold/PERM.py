# -*- coding: utf-8 -*- 

"""
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For
example, π=(5,3,2,1,4) is a permutation of length 5.
Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order).
Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

import sys
sys.path.append('../')
import rosalind_utils
import itertools

def perm():
    n = int(open("rosalind_perm.txt").read())
    print reduce(lambda x,y: x*y, xrange(1,n+1), 1)
    for p in itertools.permutations(range(1, n+1)):
        print ' '.join(map(str, list(p)))

perm()