# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:40:53 2018

@author: Memphis
"""

with open('rosalind_ba3g.txt') as input_data:
    lists =  [i.strip().split(' -> ') for i in input_data.readlines()]
cyc = dict()
for i in lists:
    cyc[i[0]] = set(i[1].split(','))

"""
based on graph theory we know the start point has one more output degree while 
end point has one more input degree. After finding these two nodes and connect them,
we transfer this problem to a cycle finding problem.
"""

#def parse_graph_edges(edge_strs):
#    graph = {}
#    for edge_str in edge_strs:
#        source, dummy, sink_str = edge_str.split(' ')
#        sinks = sink_str.split(',')
#        graph[source] = set(sinks)
#    return graph
#
#
#b = parse_graph_edges(lists)
    
def find_eulerian_path(graph):
    startnode, endnode = find_eulerian_endpoints(graph)
    if endnode in graph:
        graph[endnode].add(startnode)
    else:
        graph[endnode] = set([startnode])

    cycle, remaining_graph = find_cycle_starting_at(graph, startnode)
    while remaining_graph:
        for index, new_start in enumerate(cycle):
            if new_start in remaining_graph:
                new_cycle, remaining_graph = find_cycle_starting_at(remaining_graph, new_start)
                cycle = combine_cycles(cycle, index, new_cycle)
                break
        else:
            raise Exception("Cannot find any nodes from {} in remaining graph {}".format(cycle, remaining_graph))
    """then find the place where the help edge is added and remove it"""
    k = 0
    for i in range(len(cycle)-1):
        if cycle[i] == endnode and cycle[i+1] == startnode:
            k = i
    if k == 0:
        cy = cycle[:-1]
    else:
        cy = cycle[k+1:-1]+cycle[:k+1]
    return cy


def find_eulerian_endpoints(graph):
    indegree, outdegree = path_degrees(graph)
    startnode, endnode = None, None

    for node in indegree:
        ins, outs = indegree[node], outdegree[node]
        if outs == ins + 1:
            if startnode == None:
                startnode = node
            else:
                raise Exception("Eulerian Path would have two start nodes: {} and {}".format(startnode, node))
        elif ins == outs + 1:
            if endnode == None:
                endnode = node
            else:
                raise Exception("Eulerian Path would have two end nodes: {} and {}".format(endnode, node))

    if startnode == None or endnode == None:
        raise Exception("Could not find Eulerian Path endpoints")
    print(endnode)

    return startnode, endnode

def path_degrees(graph):
    indegree = {}
    outdegree = {}

    for source in graph:
        if source not in indegree:
            indegree[source] = 0
        outdegree[source] = len(graph[source])
        for sink in graph[source]:
            if sink in indegree:
                indegree[sink] += 1
            else:
                indegree[sink] = 1
            if sink not in outdegree:
                outdegree[sink] = 0

    return indegree, outdegree


def find_cycle_starting_at(graph, startnode):
    from random import sample

    cycle = [startnode]
    node = startnode
    complete = False
    while not complete:
        sinks = graph[node]
        next = sample(sinks, 1)[0]
        if len(sinks) > 1:
            graph[node] = sinks - set([next])
        else:
            del(graph[node])
        cycle.append(next)
        node = next
        complete = (node == startnode)
    return cycle, graph


def combine_cycles(cycle, index, new_cycle):
    cycle = cycle[:index] + new_cycle + cycle[index+1:]
    return cycle



path = find_eulerian_path(cyc)
#print(path)
print('->'.join(path))