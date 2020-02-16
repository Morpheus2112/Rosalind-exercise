# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 21:21:36 2018

@author: Memphis
"""

#!/usr/bin/env python3

def read_graph(reads):
    
    n, e = reads[0]
    adjacent_lists = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = reads[_+1]
        adjacent_lists[v1 - 1].append(v2 - 1)
    return adjacent_lists

def search(adjacent_lists, visited, leave_sequences, v):
    visited[v] = True
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            search(adjacent_lists, visited, leave_sequences, adj)
    leave_sequences.append(v)

def dfs(adjacent_lists, sources=None):
    if sources == None:
        sources = range(len(adjacent_lists))
    
    visited = [False] * len(adjacent_lists)
    leave_sequences = []
    tree_num = 0
    for source in sources:
        if not visited[source]:
            tree_num += 1
            search(adjacent_lists, visited, leave_sequences, source)
    return leave_sequences, tree_num

def is_general_sink(adjacent_lists, source):
    sources = list(range(len(adjacent_lists)))
    sources[0], sources[source] = sources[source], sources[0]
    
    return dfs(adjacent_lists, sources)[1] == 1

def find_general_sink(adjacent_lists):
    leave_sequences = dfs(adjacent_lists)[0]
    return leave_sequences[-1] if is_general_sink(adjacent_lists, leave_sequences[-1]) else None

def main():
    with open('rosalind_gs.txt') as input_data:
        k = int(input_data.readline().strip())  # Ignore first two lines.
        input_data.readline()
        edge_lists = [edges.split('\n') for edges in input_data.read().strip().split('\n\n')]
        edge_lists = [[map(int, nodes.split()) for nodes in edges[0:]] for edges in edge_lists]
#        print edge_lists
#        edge_lists = edge_lists[0]
#    
#        edges = [[],] 
#        nt = 0
#        for j in range(k):
#            lines = edge_lists[nt][1]
##            print lines
#            edges.append( edge_lists[nt:nt+ lines+1])
#    
#            nt = nt + lines + 1
##            print nt
#        edges.remove([])
    for i in edge_lists:
        h = find_general_sink(read_graph(i))
        if h:
            print h+1, 
#            print ' '.join(map(lambda v: str(v + 1), hamiltonian_path))
        else:
            print(-1),

#    print(' '.join(map(lambda v: str(v + 1) if v != None else '-1', [find_general_sink(read_graph()) for _ in range(k)])))

if __name__ == '__main__':
    main()