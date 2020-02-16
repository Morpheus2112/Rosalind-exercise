# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 00:34:59 2017

@author: Memphis
"""

import networkx as nx
import matplotlib.pyplot as plt

def cc():
    with open("rosalind_cc.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    # Create the graph
    G = nx.Graph()
    G.add_nodes_from(range(1,n+1))
    G.add_edges_from(edge_list)

    return nx.connected_components(G)

if __name__ == "__main__":
    c = cc()
    print len([len(a) for a in c])

#cc(graph){
#  let visited be a list of *false* boolean values of size N
#  CC = 0
#  for(i = 0 to N){
#    if(!visited[i]){
#     BFS(graph, visited, i);
#     CC++;
#   }
# }
# return CC;
#}