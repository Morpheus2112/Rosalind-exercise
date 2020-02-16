# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/sign/
"""

import sys
sys.path.append('../')
import rosalind_utils
import itertools

def sign():
    n = int(open("rosalind_sign.txt").read())
    print rosalind_utils.fac(n) * 2**n
    for perm in itertools.permutations(range(1, n+1)):
        perm_signs = itertools.product([1, -1], repeat=n)
        for perm_sign in perm_signs:
            print ' '.join(map(str, [sx*permx for sx,permx in zip(perm_sign, perm)]))
        
sign()