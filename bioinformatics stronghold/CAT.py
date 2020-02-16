# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/cat/
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

memo = {}

def helper(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1
    
    total = 0
    if seq in memo:
        return memo[seq]
    
    for i in xrange(1, len(seq),2):
        if ((seq[0] == 'A' and seq[i] == 'U') or
            (seq[0] == 'U' and seq[i] == 'A') or
            (seq[0] == 'C' and seq[i] == 'G') or
            (seq[0] == 'G' and seq[i] == 'C')):
            total += helper(seq[1:i]) * helper(seq[i+1:])

    memo[seq] = total % 10**6
    return memo[seq]
    
def cat():
    recs = read_fasta("rosalind_cat.txt")
    seq = recs[0][1]
    print helper(seq)

cat()