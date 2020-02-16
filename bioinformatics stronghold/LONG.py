# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/long/
"""

import sys
sys.path.append('../')
import rosalind_utils

def overlap(s,t):
    """Given two strings s and t, find the maximum overlap of s and t"""
    max_overlap = 0
    for i in xrange(len(s)):
        if t.startswith(s[-i-1:]):
            max_overlap = i+1
    return max_overlap

def head(xs):
    return xs[0]

def desc(rec):
    return rec[0]

def seq(rec):
    return rec[1]

def long():
    # recs contain the list of tuples (desc, sequence)
    recs = rosalind_utils.read_fasta("rosalind_long.txt")
    next = {}
    for reca in recs:
        for recb in recs:
            if reca == recb: continue
            min_overlap_req = min(len(seq(reca)), len(seq(recb)))
            if overlap(seq(reca), seq(recb)) > min_overlap_req / 2:
                next[reca] = recb
    # find the starting string (the one that has not in next.values())
    sub = head([rec for rec in recs if rec not in next.values()])
    merged = seq(sub)
    while sub in next:
        overlap_len = overlap(seq(sub), seq(next[sub]))
        merged += seq(next[sub])[overlap_len:]
        sub = next[sub]
    print merged

long()