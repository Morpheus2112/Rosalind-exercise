# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/rstr/
"""

import sys
from math import *
sys.path.append('../')
from rosalind_utils import *

def rstr_helper(s, gcp):
    """Given a string s and GC probability gcp, return the probability of s"""
    p = 1
    for c in s:
        p *= (gcp/2 if c in "GC" else (1-gcp)/2)
    return p

def rstr():
    with open("rosalind_rstr.txt") as f:
        toks = f.readline().strip().split()
        N = int(toks[0])
        x = float(toks[1])
        s = f.readline().strip()

    # the prob of observing string that matches with the motif
    p = rstr_helper(s, x)

    print p
    print 1 - (1-p)**N

rstr()
