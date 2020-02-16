# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/pdst/
"""

import sys
sys.path.append('../')
import rosalind_utils

def p_distance(s,t):
    return sum(1 for x,y in zip(s,t) if x!=y) / float(len(s))

def pdst():
    recs = rosalind_utils.read_fasta("rosalind_pdst.txt")
    for reca in recs:
        for recb in recs:
            print p_distance(reca[1], recb[1]),
        print ""

pdst()