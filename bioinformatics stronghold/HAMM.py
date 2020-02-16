# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 20:50:27 2017

@author: Memphis
"""

"""
Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and
t. See Figure 2.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""

import sys
sys.path.append('../')
import rosalind_utils

def hamming_distance(s,t):
    """Hamming distance"""
    return sum(1 if na!=nb else 0 for na,nb in zip(s,t))

def hamm():
    s,t = open("rosalind_hamm.txt").readlines()
    print hamming_distance(s,t)

hamm()