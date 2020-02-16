#!/usr/bin/env python3

from Queue import PriorityQueue

def read_graph(edge_list):
    
    n, e = edge_list[0]
    adjacent_lists = [[] for _ in range(n)]
    through_edge = None
    for _ in range(e):
        v1, v2, weight = edge_list[_+1]
#        print v1, v2 ,weight
        adjacent_lists[v1 - 1].append((v2 - 1, weight))
        if not through_edge:
            through_edge = (v1 - 1, v2 - 1, weight)
#    
#    print adjacent_lists
#    print through_edge
    return adjacent_lists, through_edge
#read_graph(edge_list)
def compute_min_dists(adjacent_lists, source):
    min_dists = [None] * len(adjacent_lists)
    pq = PriorityQueue()
    pq.put((0, source))
    while not pq.empty():
        min_dist, v = pq.get()
        
        if min_dists[v] != None:
            continue
        
        min_dists[v] = min_dist
        for adj, weight in adjacent_lists[v]:
            if min_dists[adj] == None:
                pq.put((min_dists[v] + weight, adj))
    return min_dists

def find_min_cycle_length(adjacent_lists, through_edge):
    from_v, to_v, weight = through_edge
    min_dists = compute_min_dists(adjacent_lists, to_v)
    return (weight + min_dists[from_v]) if min_dists[from_v] != None else -1

def main():
    with open('rosalind_cte.txt') as input_data:
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
        print find_min_cycle_length(*read_graph(edge_list)),
#    print(' '.join(map(lambda x: str(x) if x != None else '-1', [find_min_cycle_length(*read_graph()) for _ in range(k)])))

if __name__ == '__main__':
    main()