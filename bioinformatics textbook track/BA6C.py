# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:58:55 2018

@author: palan
"""
import numpy as np
def two_break_distance(P, Q):
    '''
    CODE CHALLENGE: Solve the 2-Break Distance Problem.
    Input: Genomes P and Q.
    Output: The 2-break distance d(P, Q).
    '''
    blue = colored_edges(P)
    red = colored_edges(Q)

    assert len(blue) == len(red)
    assert len(blue)+len(red) == max([element for tupl in blue+red for element in tupl])
    
    size = len(blue)+len(red) 
    
    l = colored_edges_cycles(blue,red)
    return size/2 - len(l)

def colored_edges_cycles(blue, red):
    '''    
    returns all alternating red-blue-edge cycles
    '''
    cycles = []
    size = len(blue)+len(red) 
    adj = np.zeros(shape = (size,2), dtype = np.int)
    visited = np.zeros(shape = size, dtype = np.bool)
    for e in blue:
        adj[e[0]-1,0] = e[1]-1
        adj[e[1]-1,0] = e[0]-1
    for e in red:
        adj[e[0]-1,1] = e[1]-1
        adj[e[1]-1,1] = e[0]-1
    
    for node in range(size):
        if not visited[node]:
            visited[node] = True
            head = node
            cycle = [head+1]
            # arbitrary we start with a blue edge
            color = 0
            while (True):
                node = adj[node,color]
                if (node == head):
                    # cycle found, we got back to the visited head node, 
                    # just break
                    cycles.append(cycle)
                    break
                cycle.append(node+1)
                visited[node] = True
                color = (color+1) % 2
    return cycles


def colored_edges(genome):
    '''
    CODE CHALLENGE: Implement ColoredEdges.
    Input: A genome P.
    Output: The collection of colored edges in the genome graph of P 
    in the form (x, y).
    '''
    g = []
    for p in genome:
        s = chromosome_to_cycle(p)
        for j in range(len(s)/2):
            head = 1+2*j
            tail = (2+2*j) % len(s)
            e = (s[head],s[tail])
            g.append(e)
    return g

def chromosome_to_cycle(p):
    '''
    CODE CHALLENGE: Implement ChromosomeToCycle.
    Input: A chromosome Chromosome containing n synteny blocks.
    Output: The sequence Nodes of integers between 1 and 2n resulting 
    from applying ChromosomeToCycle to Chromosome.
    '''
    nodes = []
    
    for i in p:
        if (i>0):
            nodes.append(2*i-1)
            nodes.append(2*i)
        else:
            nodes.append(-2*i)
            nodes.append(-2*i-1)
    return nodes

assert two_break_distance([[1, 2, 3, 4, 5, 6]],[[1, -3, -6, -5], [2, -4]]) == 3

def genome_str_to_list(genome):
    lp = []
    for p in genome.split('(')[1:]:
        p = permutation_str_to_list( '(' + p )
        lp.append(p)
    return lp
def permutation_str_to_list(str_p):
    p = map(int,str_p.strip()[1:-1].split(' '))
    return p

fname = 'rosalind_ba6c.txt'
lines = list(l for l in open(fname))
P = lines[0]
Q = lines[1]
P = genome_str_to_list(P)
Q = genome_str_to_list(Q)      
print two_break_distance(P,Q) 