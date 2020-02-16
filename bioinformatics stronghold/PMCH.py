# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/pmch/
Given: An RNA string s of length at most 80 bp having the same number of
occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the
bonding graph of s.
"""

import sys
sys.path.append('../')
import rosalind_utils

def num_possible_matchings(n):
    # given a graph with 2n nodes, find the possible number of perfect matchings
    if n==1:
        return 1
    return (n) * num_possible_matchings(n-1)

def pmch():
    seq = rosalind_utils.read_fasta("rosalind_pmch.txt")[0][1]
    #seq = "AGCUAGUCAU"
    num_a = seq.count('A')
    num_g = seq.count('G')
    #print num_possible_matchings(num_a)
    #print num_possible_matchings(num_g)
    return num_possible_matchings(num_a) * num_possible_matchings(num_g)

print pmch()