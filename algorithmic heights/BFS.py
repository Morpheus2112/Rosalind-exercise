# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 00:28:07 2017

@author: Memphis
"""

import networkx as nx
import matplotlib.pyplot as plt

def bfs():
    with open("rosalind_bfs.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    # Create the graph
    G = nx.DiGraph()
    G.add_nodes_from(range(1,n+1))
    G.add_edges_from(edge_list)

    dists = nx.single_source_shortest_path_length(G, 1)
    for n in G.nodes():
        print dists.get(n, -1),
    print ""
    
if __name__ == "__main__":
    bfs()
    
    
#graph is represented using adjacency list.
#
#bfs(graph, n, e, start_vertex){
#  let visited be a list of size n with false initial values.
#  let distance be list of size n with 0 initial values.
#  let Q be a queue with push, pop and front interfaces.
#  visited[start_vertex] = true;
#  Q.push(start_vertex);
#  distance[start_vertex] = 0;
#  while(!Q.empty()){
#    node_x = Q.front(); Q.pop();
#    for(i  = 0 to graph[node_x].length){
#      node_y = graph[node_x][i];
#      if(!visited[node_y]){
#        visited[node_y] = true;
#        distance[node_y] = distance[node_x] + 1;
#        Q.push(node_y);
#      }
#    }
# }
# return distance;
#}