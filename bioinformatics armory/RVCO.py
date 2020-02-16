# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 17:57:22 2018

@author: Memphis
"""

import sys
sys.path.append('../')
from rosalind_utils import *

def rvco():
    recs = read_fasta("rosalind_rvco.txt")
    return sum([1 if rec[1] == reverse_complement(rec[1]) else 0
                for rec in recs])

print rvco()