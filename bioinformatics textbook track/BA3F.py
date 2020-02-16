# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:20:55 2018

@author: Memphis
"""



def find_cycle(graph):
    from random import choice
    startnode = choice(list(graph.keys()))
    return find_cycle_starting_at(graph, startnode)


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

def find_eulerian_cycle(graph):
    cycle, remaining_graph = find_cycle(graph)
    while remaining_graph:
        for index, new_start in enumerate(cycle):
            if new_start in remaining_graph:
                new_cycle, remaining_graph = find_cycle_starting_at(remaining_graph, new_start)
                cycle = combine_cycles(cycle, index, new_cycle)
                break
        else:
            raise Exception("Cannot find any nodes from {} in remaining graph {}".format(cycle, remaining_graph))
    return cycle




with open('rosalind_ba3f.txt') as input_data:
    lists =  [i.strip().split(' -> ') for i in input_data.readlines()]
cyc = dict()
for i in lists:
    cyc[i[0]] = set(i[1].split(','))
    
b = find_eulerian_cycle(cyc)
print('->'.join(b))