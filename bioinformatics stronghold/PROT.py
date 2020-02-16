# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:34:25 2017

@author: Memphis
"""

"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from
the English alphabet (all letters except for B, J, O, U, X, and Z). Protein
strings are constructed from these 20 symbols. Henceforth, the term genetic
string will incorporate protein strings along with DNA strings and RNA strings.
The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output
MAMAPRTEINSTRING
"""

import sys
sys.path.append('../')
import rosalind_utils

def prot():
    mrna = open("rosalind_prot.txt").read().strip()
    print rosalind_utils.translate(mrna)

prot()