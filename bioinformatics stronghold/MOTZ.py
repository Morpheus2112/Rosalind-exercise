# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/motz/
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

memo = {}
def helper(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1

    if seq in memo:
        return memo[seq]

    memo[seq] = helper(seq[1:])
    for i in xrange(1, len(seq)):
        if ((seq[0] == 'A' and seq[i] == 'U') or
            (seq[0] == 'U' and seq[i] == 'A') or
            (seq[0] == 'C' and seq[i] == 'G') or
            (seq[0] == 'G' and seq[i] == 'C')):
            memo[seq] += helper(seq[1:i]) * helper(seq[i+1:])
    memo[seq] %= 10**6
    return memo[seq]
        

def motz():
    recs = read_fasta("rosalind_motz.txt")
    seq = recs[0][1]
    print helper(seq)

motz()