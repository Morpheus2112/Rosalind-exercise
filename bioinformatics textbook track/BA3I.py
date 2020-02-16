# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 22:28:29 2018

@author: Memphis
"""


def eulerian_cycle(edge_dict):
    '''Generates an Eulerian cycle from the given edges.'''
    current_node = edge_dict.keys()[0]
    path = [current_node]

    # Get the initial cycle.
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break

    # Continually expand the initial cycle until we're out of edge_dict.
    while len(edge_dict) > 0:
        for i in xrange(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path

from itertools import product

# Read the input data.
with open('rosalind_ba3i.txt') as input_data:
    k = int(input_data.read().strip())


# Create the edges.
universal_dict = {}
for kmer in [''.join(item) for item in product('01', repeat=k)]:
    if kmer[:-1] in universal_dict:
        universal_dict[kmer[:-1]].append(kmer[1:])
    else:
        universal_dict[kmer[:-1]] = [kmer[1:]]

# Get the cycle, remove the repeated last entry for the associated path.
path = eulerian_cycle(universal_dict)

# Print and save the answer.
print ''.join([item[0] for item in path[:-1]])
with open('3i.txt', 'w') as output_data:
    output_data.write(''.join([item[0] for item in path[:-1]]))