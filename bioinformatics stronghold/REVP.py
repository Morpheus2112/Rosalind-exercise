# -*- coding: utf-8 -*- 

"""
see http://rosalind.info/problems/revp/
"""

import sys
sys.path.append('../')
import rosalind_utils

def revp():
    # get the sequence of the only entry
    seq = rosalind_utils.read_fasta("rosalind_revp.txt")[0][1] 
    for l in xrange(4,13):
        # find all reverse palindromes of length l
        for i in range(len(seq)-l+1):
            # if reverse palindrome, report the position and length
            if seq[i:i+l] == rosalind_utils.reverse_complement(seq[i:i+l]):
                print i+1, l
    
revp()