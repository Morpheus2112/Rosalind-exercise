# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/eval/
"""

import sys
sys.path.append('../')
from rosalind_utils import *

def helper(s, gc):
    """probability of observing s for a given GC dist"""
    p = 1
    for c in s:
        p *= (gc/2 if c in "GC" else (1-gc)/2)
    return p
    
def _eval():
    with open("rosalind_eval.txt") as f:
        n = int(f.readline())
        s = f.readline().strip()
        A = map(float, f.readline().split())

    for a in A:
        print helper(s, a) * (n-len(s)+1),

_eval()