# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 16:54:51 2018

@author: Memphis
"""



import sys
sys.path.append('../')
from rosalind_utils import *
from Bio.Seq import translate

def ptra():
    with open("rosalind_ptra.txt") as f:
        dna = f.readline().strip()
        prot = f.readline().strip()
#
    print dna
#    print prot

    t= [1,2,3,4,5,6,9,10,11,12,13,14,15,16]
    for i in t:
        if translate(dna, table=i, to_stop=True) == prot:
            return i

    
print ptra()