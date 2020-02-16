# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/aspc/
"""

import sys
sys.path.append('../')
import rosalind_utils

def aspc():
    n, m = map(int, open("rosalind_aspc.txt").readline().split())
    # print n, m
    s = 0
    for k in range(m, n+1) :
        s = (s + rosalind_utils.choose_large(n,k)) % 10**6
    return s

print aspc()