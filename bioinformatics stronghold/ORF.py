# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/orf/
"""

import sys
sys.path.append('../')
from rosalind_utils import *

def orf():
    # read sequence from fasta file
    seq = read_fasta("rosalind_orf.txt")[0][1]
    reading_frames = [translate(transcribe(seq)),
                      translate(transcribe(seq[1:])),
                      translate(transcribe(seq[2:])),
                      translate(transcribe(reverse_complement(seq))),
                      translate(transcribe(reverse_complement(seq)[1:])),
                      translate(transcribe(reverse_complement(seq)[2:]))]
    all_orfs = set()
    for rf in reading_frames:
        # find all positions of 'M' and all positions of '*' (start and stop codons)
        start_codons = [i for i in range(len(rf)) if rf[i]=='M']
        stop_codons = [i for i in range(len(rf)) if rf[i]=='*']
        for start in start_codons:
            for stop in stop_codons:
                # if there is no other stop codon within the string, it is ORF
                if start < stop and '*' not in rf[start:stop]:
                    all_orfs.add(rf[start:stop])
    print '\n'.join(all_orfs)

orf()