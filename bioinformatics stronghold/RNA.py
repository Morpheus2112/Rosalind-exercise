# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:28:43 2017

@author: Memphis
"""

"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u
is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""

def rna():
    dna_seq = open("rosalind_rna.txt").read().strip()
    transcribe = {'A':'A', 'C':'C', 'G':'G', 'T':'U'}
    rna_seq = ''.join(transcribe[nuc] for nuc in dna_seq)
    return rna_seq
    
#print rna()