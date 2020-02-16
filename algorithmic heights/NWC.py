# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 20:38:42 2018

@author: Memphis
"""

#!/usr/bin/env python3
def read_graph(edge_list):
    
    n, e = edge_list[0]
    edges = []
    for _ in range(e):
        v1, v2, weight = edge_list[_+1]
#        print v1, v2 ,weight
        edges.append((v1 - 1, v2 - 1, weight))
    return n, edges
#def read_graph():    
#    while True:
#        line = input()
#        if line != '':
#            break
#    n, e = map(int, line.split())
#    edges = []
#    for _ in range(e):
#        v1, v2, weight = map(int, input().split())
#        edges.append((v1 - 1, v2 - 1, weight))
#    return n, edges

def relax(min_dists, edges):
    changed = False
    for from_v, to_v, weight in edges:
        if min_dists[from_v] != None and (min_dists[to_v] == None or min_dists[to_v] > min_dists[from_v] + weight):
            min_dists[to_v] = min_dists[from_v] + weight
            changed = True
    return changed

def has_negative_weight_cycle_from_source(n, edges, source):
    min_dists = [None] * n
    min_dists[source] = 0
    
    for _ in range(n - 1):
        relax(min_dists, edges)
    
    return relax(min_dists, edges), set(filter(lambda v: min_dists[v] != None, range(n)))

def has_negative_weight_cycle(n, edges):
    sources = set(range(n))
    while sources:
        source = next(iter(sources))
        negative_weight_cycle, reachable_vertices = has_negative_weight_cycle_from_source(n, edges, source)
        
        if negative_weight_cycle:
            return True
        
        sources -= reachable_vertices
        edges = list(filter(lambda edge: edge[0] not in reachable_vertices and edge[1] not in reachable_vertices, edges))
    return False

def main():
    with open('rosalind_nwc.txt') as input_data:
        input_data.readline()  # Ignore first two lines.

        edge_lists = [edges.split('\n') for edges in input_data.read().strip().split('\n\n')]
        edge_lists = [[map(int, nodes.split()) for nodes in edges[0:]] for edges in edge_lists]
        edge_lists = edge_lists[0]
        i = 0
        edges = [[],]
        for j in range(len(edge_lists)-1):
            j += 1
            if len(edge_lists[j]) == 2:
                edges.append(edge_lists[i:j])
                i = j
        edges.append(edge_lists[i:])
        edges.pop(0)
    for edge_list in edges:
        print '1' if has_negative_weight_cycle(*read_graph(edge_list)) else '-1',
            

#    print(' '.join(['1' if has_negative_weight_cycle(*read_graph()) else '-1' for _ in range(k)]))

if __name__ == '__main__':
    main()