# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 13:02:32 2018

@author: Memphis
"""


from math import *
import sys
sys.path.append('../')
from rosalind_utils import *
import StringIO

def phre():
    with open("rosalind_phre.txt") as f:
        th = int(f.readline())
        fastq = f.read()

    with open("foo.fastq", 'w') as f:
        f.write(fastq)

    records = SeqIO.parse("foo.fastq", "fastq")

    num_rec = 0 # num records whose avg quality is below threshold
    for rec in records:
        qs = rec.letter_annotations['phred_quality']
        if float(sum(qs)) / len(qs) < th:
            num_rec += 1

    print num_rec

if __name__ == '__main__':
    phre()