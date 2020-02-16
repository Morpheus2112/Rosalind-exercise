# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/lcsm/
"""

import sys
sys.path.append('../')
from rosalind_utils import *

def lcsm():
    recs = read_fasta("rosalind_lcsm.txt")
    seqs = [rec[1] for rec in recs]
    common_substrs = {seqs[0]}
    for seq in seqs[1:]:
        new_set = set()
        for common_substr in common_substrs:
            new_set = new_set.union(longest_common_substring(common_substr, seq))
        common_substrs = new_set

    return max(common_substrs, key=lambda x: len(x))

print lcsm()