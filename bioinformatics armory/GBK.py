# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 10:08:55 2018

@author: Memphis
"""



import sys
sys.path.append('../')
from rosalind_utils import *
from Bio import Entrez
Entrez.email = "zhangjichang.pku@gmail.com"

def gbk():
    genus, date_a, date_b = map(lambda line: line.strip(),
                                open("rosalind_gbk.txt").readlines())
    term = '%s[Organism] AND ("%s"[PDAT] : "%s"[PDAT])' % (genus, date_a, date_b)
    print term
    
    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    handle.close()
    return int(record["Count"])

print gbk()
