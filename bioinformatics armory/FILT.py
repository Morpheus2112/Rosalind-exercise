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
    with open("rosalind_filt.txt") as f:
        q, p = map(int, f.readline().split())
        fastq = f.read()
    with open("foo.fastq", 'w') as f:
        f.write(fastq)

    num_filtered = 0
    recs = SeqIO.parse("foo.fastq", "fastq")
#    print list(recs)
    for rec in recs:
        quals = rec.letter_annotations["phred_quality"]
        # find num of bases above quality threshold
#        print quals
        nb = sum([1 if b >= q else 0 for b in quals])
#        print nb,
#        print len(quals) * p / 100.0
        if nb >= len(quals) * p / 100.0:
#            print len(quals) * p / 100.0
#            print True
            num_filtered += 1

    print num_filtered

if __name__ == '__main__':
    filt()
