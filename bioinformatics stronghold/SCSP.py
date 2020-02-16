# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/scsp/
"""

import sys
sys.path.append('../')
from rosalind_utils import *

VERY_LARGE_INT = 10**15

def subsequence_check(s, t):
    """Check if s in t"""
    idx = 0
    for let in s:
        idx = t.find(let)
        if idx == -1: return False
    else:
        return True

LOOKUP_TABLE = {(0,0): ("","")} # memoization to store shortest alignment at some point

def shortest_alignment(C, s, t, i, j):
    """Given a scoring table C and sequences s and t, find the all possible optimum
    alignments.
    cur_algns: list of current alignments up to this point"""
    if (i,j) not in LOOKUP_TABLE:
        if j == 0:
            algn_a, algn_b = shortest_alignment(C,s,t,i-1,j)
            LOOKUP_TABLE[(i,j)] = (algn_a+s[i-1], algn_b+'-')
        elif i == 0:
            algn_a, algn_b = shortest_alignment(C,s,t,i,j-1)
            LOOKUP_TABLE[(i,j)] = (algn_a+'-', algn_b+t[j-1])
        else:
            ret = []
            if C[i][j] == C[i-1][j] + 1:
                algn_a, algn_b = shortest_alignment(C,s,t,i-1,j)
                ret.append((algn_a+s[i-1], algn_b+'-'))
            if C[i][j] == C[i][j-1] + 1:
                algn_a, algn_b = shortest_alignment(C,s,t,i,j-1)
                ret.append((algn_a+'-', algn_b+t[j-1]))
            if C[i][j] == C[i-1][j-1] and s[i-1] == t[j-1]:
                algn_a, algn_b = shortest_alignment(C,s,t,i-1,j-1)
                ret.append((algn_a+s[i-1], algn_b+t[j-1]))
            LOOKUP_TABLE[(i,j)] = min(ret, key=lambda (a,b): len(a))
            
    return LOOKUP_TABLE[(i,j)]

def scsp():
    seqa, seqb = open("rosalind_scsp.txt").read().split()
    C = edit_distance_helper(seqa, seqb, sub_pen=VERY_LARGE_INT)
    #print seqa
    #print seqb
    #for row in C: print row
    # select the shortest alignment
    shortest_algn = shortest_alignment(C, seqa, seqb, len(seqa), len(seqb))
    print '\n'.join(shortest_algn)
    print ''.join(shortest_algn[0][i]
                  if shortest_algn[0][i] != '-' else shortest_algn[1][i]
                  for i in xrange(len(shortest_algn[0])))
scsp()