# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/edit/
"""

import sys
sys.path.append('../')
from rosalind_utils import *

# edit distance is same as the length of longest common subsequence
def edit():
    recs = read_fasta("rosalind_edit.txt")
    seqa, seqb = recs[0][1], recs[1][1]
    return edit_distance(seqa, seqb)


print edit()