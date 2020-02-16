# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/splc/
"""

import sys
sys.path.append('../')
import rosalind_utils

def splc():
    recs = rosalind_utils.read_fasta("rosalind_splc.txt")
    seqs = [rec[1] for rec in recs]

    exon = seqs[0]
    introns = sorted(seqs[1:], key=lambda(s): len(s), reverse=True)
    #print introns
    for intron in introns:
        exon = exon.replace(intron, "", 1)
    prot =  rosalind_utils.translate(rosalind_utils.transcribe(exon))
    return prot[:-1]

print splc()