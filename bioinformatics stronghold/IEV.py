# -*- coding: utf-8 -*- 

"""
problem description at http://rosalind.info/problems/iev/
"""


def iev():
    L = map(int, open("rosalind_iev.txt").read().split())
    print (4*L[0] + 4*L[1] + 4*L[2] + 3*L[3] + 2*L[4]) / 2.0


iev()