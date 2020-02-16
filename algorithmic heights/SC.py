# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 22:27:01 2018

@author: Memphis
"""


def read_graph(reads):
    
    n, e = reads[0]
    adjacent_lists = [[] for _ in range(n)]
    edges = set()
    for _ in range(e):
        v1, v2 = reads[_+1]
        adjacent_lists[v1 - 1].append(v2 - 1)
        edges.add((v1 - 1, v2 - 1))
    return adjacent_lists, edges

def search(adjacent_lists, visited, leave_sequences, tree_set, v):
    visited[v] = True
    for adj in adjacent_lists[v]:
        if not visited[adj]:
            search(adjacent_lists, visited, leave_sequences, tree_set, adj)
    leave_sequences.append(v)
    tree_set.add(v)

def dfs(adjacent_lists, sources=None):
    if sources == None:
        sources = range(len(adjacent_lists))
    
    visited = [False] * len(adjacent_lists)
    leave_sequences = []
    tree_sets = []
    for source in sources:
        if not visited[source]:
            tree_set = set()
            search(adjacent_lists, visited, leave_sequences, tree_set, source)
            tree_sets.append(tree_set)
    return leave_sequences, tree_sets

def reverse_graph(adjacent_lists):
    reversed_adjacent_lists = [[] for _ in range(len(adjacent_lists))]
    for from_v in range(len(adjacent_lists)):
        for to_v in adjacent_lists[from_v]:
            reversed_adjacent_lists[to_v].append(from_v)
    return reversed_adjacent_lists

def find_strongly_connected_components(adjacent_lists):
    leave_sequences = dfs(adjacent_lists)[0]
    return dfs(reverse_graph(adjacent_lists), leave_sequences[::-1])[1]

def has_edge_between(edges, from_strongly_connected_component, to_strongly_connected_component):
    for from_v in from_strongly_connected_component:
        for to_v in to_strongly_connected_component:
            if (from_v, to_v) in edges:
                return True
    return False

def is_semi_connected(adjacent_lists, edges):
    strongly_connected_components = find_strongly_connected_components(adjacent_lists)
    
    for i in range(len(strongly_connected_components) - 1):
        if not has_edge_between(edges, strongly_connected_components[i], strongly_connected_components[i + 1]):
            return False
    return True

def main():
    with open('rosalind_sc.txt') as input_data:
        k = int(input_data.readline().strip())  # Ignore first two lines.
        input_data.readline()
        edge_lists = [edges.split('\n') for edges in input_data.read().strip().split('\n\n')]
        edge_lists = [[map(int, nodes.split()) for nodes in edges[0:]] for edges in edge_lists]
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
#    
    for i in edge_lists:
        hamiltonian_path = is_semi_connected(*read_graph(i))
        if hamiltonian_path:
            print '1', 
            
        else:
            print '-1',
#    k = int(input())
#    print(' '.join(['1' if is_semi_connected(*read_graph()) else '-1' for _ in range(k)]))

if __name__ == '__main__':
    main()