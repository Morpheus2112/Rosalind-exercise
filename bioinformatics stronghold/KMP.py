# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 22:51:52 2018

@author: Memphis
"""

# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/kmp/
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

def kmp_table(w):
    # see en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
    T = [None] * (len(w)+1)
    T[0] = -1
    T[1] = 0
    pos = 2
    cnd = 0
    while pos <= len(w):
        if w[pos-1] == w[cnd]:
            cnd += 1
            T[pos] = cnd
            pos += 1
        elif cnd > 0:
            cnd = T[cnd]
        else:
            T[pos] = 0
            pos += 1
    return T

    
def kmp():
    rec = read_fasta("rosalind_kmp.txt")
    t = kmp_table(rec[0][1])
    print " ".join(map(str, t[1:]))

kmp()