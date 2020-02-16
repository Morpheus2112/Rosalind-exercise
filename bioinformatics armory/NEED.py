# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 10:37:55 2018

@author: Memphis
"""

"""
first need to install Emboss?
"""


import sys
sys.path.append('../')
from rosalind_utils import *
from Bio import Entrez
Entrez.email = "palandswd@gmail.com"
from Bio.Emboss.Applications import NeedleCommandline

def dl_seq(id):
    handle = Entrez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record.seq.tostring()

def need():
    genbank_ids = open("rosalind_need.txt").read().split()
    seqa = dl_seq(genbank_ids[0])
    seqb = dl_seq(genbank_ids[1])
    with open("seqa.faa", 'w') as f:
        f.write('>seqa\n%s\n' % seqa)
    with open("seqb.faa", 'w') as f:
        f.write('>seqb\n%s\n' % seqb)
#    needle_cline = "needle -asequence ./seqa.faa -bsequence ./seqb.faa -gapopen 10 -gapextend 1 -outfile needle.txt -endweight -endopen 10 -endextend 1"
#
#    import os
#    os.system(needle_cline)


    
need()