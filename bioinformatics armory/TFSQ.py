# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 10:48:26 2018

@author: Memphis
"""


from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

def tfsq():
    handle = open("rosalind_tfsq.txt")
    records = SeqIO.parse(handle, "fastq")
    output_handle = open("rosalind_out.txt", 'w')
    SeqIO.write(records, output_handle, "fasta")
tfsq()