# -*- coding: utf-8 -*- 

"""
see http://rosalind.info/problems/seto/
"""

import sys
sys.path.append('../')
import rosalind_utils

def print_set(st):
    print '{%s}' % ', '.join(map(str, st))
    

def seto():
    lines = open("rosalind_seto.txt").readlines()
    n = int(lines[0])
    A = eval(lines[1])
    B = eval(lines[2])
    universal = set(range(1, n+1))

    print_set(A.union(B))
    print_set(A.intersection(B))
    print_set(A.difference(B))
    print_set(B.difference(A))
    print_set(universal.difference(A))
    print_set(universal.difference(B))


seto()