# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:43:47 2018

@author: Memphis
"""
with open('rosalind_ba4d.txt') as input_data:
    
    i = int(input_data.readline().strip())
    

aminoacid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def peptides(n, d):
    for m in aminoacid_masses:
        if n-m in d:
            d[n] = d.get(n,0)+d[n-m]
    return d


def pep_counter(M):
    dicc = {0:1}
    mn = min(aminoacid_masses)
    for i in range(M-mn+1):
        j = i+mn
        peptides(j,dicc)
    return dicc


# This line calls the routine and indexes the returned dict.  Both with the desired mass (the mass we want peptides to sum up to)
print(pep_counter(i)[i])