# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 01:16:52 2017

@author: Memphis
"""

import networkx as nx
import matplotlib.pyplot as plt

def bip():
    with open("rosalind_bip.txt") as f:
        lines = f.readlines()
        # remove empty lines
        lines = [line for line in lines if line.strip()]

    # Num test cases
    t = int(lines[0])
    del lines[0]
    for i in xrange(t):
        n, e = map(int, lines[0].split())
        edge_list = map(lambda x: map(int, x.strip().split()), lines[1:e+1])
        del lines[:e+1]

        # Create the graph
        G = nx.Graph()
        G.add_nodes_from(range(1,n+1))
        G.add_edges_from(edge_list)

        if nx.is_bipartite(G):
            print 1,
        else:
            print -1,
    print ""
    
if __name__ == "__main__":
    bip()
    

#For each v in V
#    Set colour(v) = undefined
#
#Pick a vertex w
#Set colour(w) = 0
#
#Let q be a queue
#Push w onto q
#
#While q is not empty
#    Pop u from q
#    For each edge from u to v
#        If colour(u) == colour(v) then
#            Return False
#        Else if colour(v) == undefined then
#            colour(v) = 1 - colour(u)
#            Push v onto q
#
#Return True