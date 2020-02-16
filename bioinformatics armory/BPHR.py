# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 16:24:16 2018

@author: Memphis
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

def filt():
    with open("rosalind_bphr.txt") as f:
        q = int(f.readline().strip())
        fastq = f.read()
    with open("foo.fastq", 'w') as f:
        f.write(fastq)

    recs = SeqIO.parse("foo.fastq", "fastq")
    
    total = [[],] 
    for rec in recs:
        quals = rec.letter_annotations["phred_quality"]
        # find num of bases above quality threshold
#        print quals
        total.append(quals)
    total.remove([])
    n = len(total)
#    print n
    l = len(total[0])
#    print l
    pos = 0
    for i in range(l):
        m = 0
        for j in range(n):
            m = m + total[j][i]
#        print m, m/n,q
        if m/n < q:
            pos += 1
    print pos

if __name__ == '__main__':
    filt()
