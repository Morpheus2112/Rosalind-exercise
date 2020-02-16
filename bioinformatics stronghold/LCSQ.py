# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/lcsq/
"""

import sys
sys.path.append('../')
import rosalind_utils

import sys
sys.setrecursionlimit(1500)

# important: the longest common subsequence algorithm is implemented recursively. For
# running on large sequences, it may exceed maximum recusion depth. Lazy way to solve
# this issue is to increase the recursion depth limit
# sys.setrecursionlimit(1500)

def lcsq():
    recs = rosalind_utils.read_fasta("rosalind_lcsq.txt")
    seqa, seqb = recs[0][1], recs[1][1]
    # return the set of all longest common subsesquences
    C = rosalind_utils.lcsq(seqa, seqb)
    print rosalind_utils.lcsq_len(C)
    print rosalind_utils.lcsq_backtrack(C, seqa, seqb, len(seqa), len(seqb))

lcsq()