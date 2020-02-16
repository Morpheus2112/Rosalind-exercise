# -*- coding: utf-8 -*- 

"""
see http://rosalind.info/problems/tree/
"""



# The number of edges required is N-E-1,
# where N is the number of nodes and E is the number of edges.
def tree():
    lines = open("rosalind_tree.txt").read().splitlines()
    n = int(lines[0])
    e = len(lines)-1
    return n-e-1

print tree()
