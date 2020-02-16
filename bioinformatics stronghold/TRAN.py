# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/tran/
"""

import sys
sys.path.append('../')
import rosalind_utils


def tran():
    recs = rosalind_utils.read_fasta("rosalind_tran.txt")
    seqs = [rec[1] for rec in recs]

    purines = "AG"
    pyrimidines = "CT"
    
    transition = 0
    transversion = 0
    for a,b in zip(seqs[0], seqs[1]):
        if a==b:
            continue
        
        elif ((a in purines and b in purines) or
            (a in pyrimidines and b in pyrimidines)):
            transition += 1
        else:
            transversion += 1

    return float(transition) / transversion

print tran()