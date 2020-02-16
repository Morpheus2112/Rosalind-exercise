# -*- coding: utf-8 -*- 

"""
see http://rosalind.info/problems/sset/
"""


def sset():
    n = int(open("rosalind_sset.txt").read())
    return 2**n % 10**6

print sset()