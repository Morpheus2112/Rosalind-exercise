# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 10:33:08 2018

@author: Memphis
"""



import sys
sys.path.append('../')
from rosalind_utils import *

from Bio import Entrez
Entrez.email = "zhangjichang.pku@gmail.com"

def frmt():
    ids = open("rosalind_frmt.txt").read().split()
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()
#    print records
    shortest_rec = min(records, key=lambda rec: len(rec.seq))
    print shortest_rec.format("fasta")

frmt()