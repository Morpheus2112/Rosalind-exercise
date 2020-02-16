# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/kmer/
"""

import sys
sys.path.append('../')
import itertools
import rosalind_utils

def overlapping_count(s, t, cur_cnt):
    index = s.find(t)
    if index > -1:
        return overlapping_count(s[index+1:], t, cur_cnt+1)
    else:
        return cur_cnt

def kmer():
    seq = rosalind_utils.read_fasta("rosalind_kmer.txt")[0][1]
    rev_comp = rosalind_utils.reverse_complement(seq)
    for mer in itertools.product("ACGT", repeat=4):
        s = ''.join(mer)
        print overlapping_count(seq, s, 0),
    print ""

print kmer()