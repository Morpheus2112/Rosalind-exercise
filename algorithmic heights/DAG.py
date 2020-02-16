# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:00:18 2017

@author: Memphis
"""

import networkx as nx
import matplotlib.pyplot as plt

def dag():
    with open("rosalind_dag.txt") as f:
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
        G = nx.DiGraph()
        G.add_nodes_from(range(1,n+1))
        G.add_edges_from(edge_list)
        print G
        if nx.is_directed_acyclic_graph(G):
            print 1,
        else:
            print -1,
    print ""
    

if __name__ == "__main__":
    dag()

#
#cycle_found = false
#let visited be a list of boolean false value of size V.
#
#has_cycle(graph, start_vertex){
#  if(cycle_found)
#    return;
#  visited[start_vertex] = true;
#  for(i = 0 to graph[start_vertex].length){
#    node_y = graph[start_vertex][i]
#    if(!visited[node_y] && !cycle_found){
#      has_cycle(graph, node_y);
#    }
#    else{
#      cycle_found = true;
#    }
#  }
#}