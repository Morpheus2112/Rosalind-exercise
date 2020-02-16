# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/lgis/
"""

import sys
sys.path.append('../')
from rosalind_utils import *

def print_list(L):
    print ' '.join(map(str, L))
    
def lgis():
    with open("rosalind_lgis.txt") as f:
        f.readline() # n: no need
        nums = map(int, f.readline().split())

    inc_seq = LGIS(nums)
    print_list(inc_seq)
    
    nums.reverse()
    dec_seq = LGIS(nums)
    dec_seq.reverse()
    print_list(dec_seq)

lgis()