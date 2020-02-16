# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/sseq/
"""

import sys
sys.path.append('../')
import rosalind_utils

def sseq():
    recs = rosalind_utils.read_fasta("rosalind_sseq.txt")
    s = recs[0][1]
    t = recs[1][1]
    last_index = 0
    # assuming t is a substring of s (not necessarily contiguously)
    for tlet in t:
        idx = s[last_index:].find(tlet)
        print last_index+idx+1,
        last_index += idx+1
    print ""

sseq()