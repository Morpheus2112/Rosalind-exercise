# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 13:45:01 2018

@author: palan
"""

def two_break_sorting(P,Q):
    '''
    CODE CHALLENGE: Solve the 2-Break Sorting Problem.     
    2-Break Sorting Problem: Find a shortest transformation 
    of one genome into another via 2-breaks.
    Input: Two genomes with circular chromosomes on the same 
    set of synteny blocks.
    Output: The collection of genomes resulting from applying 
    a shortest sequence of 2-breaks transforming one genome into the other.
    '''
    red = colored_edges(Q)
    path = [P]
    while two_break_distance(P,Q) > 0:
        cycles = colored_edges_cycles(colored_edges(P),red)
        for c in cycles:
            if len(c) >= 4:
                P = two_break_on_genome(P,c[0],c[1],c[3],c[2])
                path.append(P)
                break          
    return path

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


def two_break_on_genome_graph(g,i,j,k,l):
    '''
    CODE CHALLENGE: Implement 2-BreakOnGenomeGraph.
    Input: The colored edges of a genome graph GenomeGraph, 
    followed by indices i, j, k, and l.
    Output: The colored edges of the genome graph resulting from applying 
    the 2-break operation 2-BreakOnGenomeGraph(GenomeGraph, i, j, k, l).
    '''
    bg = []
    # equivalent and more elegant but not accepted by the grader ...
#    d = {(i,j):(i,k), (j,i):(j,l), (k,l):(k,i), (l,k):(l,j)}    
#    for t in g:
#        if (t in d):
#            bg.append(d[t])
#        else:
#            bg.append(t)
    
    # so do it this way
    rem = ((i,j), (j,i), (k,l), (l,k))
    bg = [ t for t in g if t not in rem]
    bg.append((i,k))
    bg.append((j,l))
    
    return bg

def two_break_on_genome(genome,i,j,k,l):
    '''
    CODE CHALLENGE: Implement 2-BreakOnGenome.
    Input: A genome P, followed by indices i, i', j, and j'.
    Output: The genome P' resulting from applying the 2-break operation
    2-BreakOnGenomeGraph(GenomeGraph, i, i′, j, j′).
    '''
    g = colored_edges(genome)
    g = two_break_on_genome_graph(g,i,j,k,l)
    genome = graph_to_genome(g)
    return genome
def graph_to_genome(g):
    '''
    CODE CHALLENGE: Implement GraphToGenome.
    Input: The colored edges ColoredEdges of a genome graph.
    Output: The genome P corresponding to this genome graph.
    '''
    
    genome = []
    visit = []
    adj = np.zeros(len(g)*2, dtype = np.int)
    for t in g:
        adj[t[0]-1] = t[1]-1
        adj[t[1]-1] = t[0]-1
    
    for t in g:
        orig = t[0]
        if orig in visit:
            continue
        visit.append(orig)
        if (orig%2 == 0):
            closing = orig-1
        else:
            closing = orig+1
        p = []
        i = 0
        while(True):
            if (orig%2 == 0):
                p.append(orig/2)
            else:
                p.append(-(orig+1)/2)
            dest = adj[orig-1]+1
            i = i + 1
            if (i>100):
                assert False
                return
            visit.append(dest)
            if (dest == closing):
                genome.append(p)
                break
            if (dest%2 == 0):
                orig = dest -1
            else:
                orig = dest + 1
            assert orig > 0
            visit.append(orig)
    return genome

def format_sequence(s):
    fs = []
    for p in s:
        str_p = permutation_list_to_str(p)
        fs.append(str_p)
    return fs
def permutation_list_to_str(p):
    def str_val(i):
        if (i>0):
            return '+'+str(i)
        else:
            return str(i)
    return '(' + ' '.join(map(str_val,p)) + ')'

P = '(-5 +3 -4 +12 +13 +2 +1 -11 -8 +10 +7 -6 +9)'
Q = '(-3 +13 -9 +8 +4 -12 -5 -1 +6 +10 -2 +7 +11)'
P = genome_str_to_list(P)
Q = genome_str_to_list(Q)
path = two_break_sorting(P,Q)
print '\n'.join([''.join(format_sequence(p)) for p in path])