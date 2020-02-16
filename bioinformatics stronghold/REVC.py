# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:32:10 2017

@author: Memphis
"""

"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and
'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the
symbols of s, then taking the complement of each symbol (e.g., the reverse complement
of"GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
"""

import sys
sys.path.append('../')
import rosalind_utils

def revc():
    dna = open("rosalind_revc.txt").read().strip()
    print rosalind_utils.reverse_complement(dna)
    
revc()