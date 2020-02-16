# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/spec/
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

mass_table = {
'A':   71.03711,
'C':   103.00919,
'D':   115.02694,
'E':   129.04259,
'F':   147.06841,
'G':   57.02146,
'H':   137.05891,
'I':   113.08406,
'K':   128.09496,
'L':   113.08406,
'M':   131.04049,
'N':   114.04293,
'P':   97.05276,
'Q':   128.05858,
'R':   156.10111,
'S':   87.03203,
'T':   101.04768,
'V':   99.06841,
'W':   186.07931,
'Y':   163.06333
}

def is_equal(a,b):
    eps = 0.000001
    return abs(a-b) < eps

def spec():
    prot = ""
    weights = map(float, open("rosalind_spec.txt").read().strip().split('\n'))
    for i in xrange(len(weights)-1):
        dif = weights[i+1] - weights[i]
        lets = [let for let in mass_table.keys() if is_equal(dif, mass_table[let])]
        assert len(lets) > 0
        prot = prot + lets[0]

    print prot

spec()