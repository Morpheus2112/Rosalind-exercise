# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:08:52 2017

@author: Memphis
"""

import networkx as nx
import matplotlib.pyplot as plt

def dij():
    r = []
    with open("rosalind_dij.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    # Create the graph
    G = nx.DiGraph()
    G.add_nodes_from(range(1,n+1))
    G.add_weighted_edges_from(edge_list)

    for n in G.nodes():
        try:
            r.append(nx.dijkstra_path_length(G, 1, n))
        except:
            # node is not reachable
            r.append(-1),
#    return r
    return ' '.join(map(str,r))
    
if __name__ == "__main__":
    s = dij()
    with open('output_dij.txt','w') as g:
        g.write(s)