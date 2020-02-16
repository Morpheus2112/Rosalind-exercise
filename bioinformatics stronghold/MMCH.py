# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/mmch/
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

def num_matches(seq):
    """Return the total possible number of maximum matchings of basepair edges
    in the bonding graph of s."""
    na = seq.count('A')
    nu = seq.count('U')
    nc = seq.count('C')
    ng = seq.count('G')
    return (perm(max(na,nu), min(na,nu)) *
            perm(max(nc,ng), min(nc,ng)))

def mmch():
    recs = read_fasta("rosalind_mmch.txt")
    seq = recs[0][1]
    print num_matches(seq)

mmch()