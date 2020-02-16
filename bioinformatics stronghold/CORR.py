# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/corr/
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

def corr():
    recs = read_fasta("rosalind_corr.txt")
    seqs = [rec[1] for rec in recs]
    # case 1: s was correctly sequenced in the dataset (or its reverse comp.)
    correct_seqs = []
    incorrect_seqs = []
    for seq in seqs:
        cnts = seqs.count(seq) + seqs.count(reverse_complement(seq))
        if seq == reverse_complement(seq):
            # if palindrome, count it only once
            cnts -= 1
        if cnts > 1:
            if (seq not in correct_seqs and
                reverse_complement(seq) not in correct_seqs):
                correct_seqs.append(seq)
        else:
            incorrect_seqs.append(seq)

    for inc_seq in incorrect_seqs:
        for cor_seq in correct_seqs:
            if hamming_distance(inc_seq, cor_seq) == 1:
                mut_seq = cor_seq
                break
            elif hamming_distance(inc_seq, reverse_complement(cor_seq)) == 1:
                mut_seq = reverse_complement(cor_seq)
                break
        else:
            assert False, "shouldn't be here."
                
        print "%s->%s" % (inc_seq, mut_seq)

corr()