# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:50:22 2018

@author: palan
"""


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

def permutation_str_to_list(str_p):
    p = map(int,str_p.strip()[1:-1].split(' '))
    return p

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

def genome_str_to_list(genome):
    lp = []
    for p in genome.split('(')[1:]:
        p = permutation_str_to_list( '(' + p )
        lp.append(p)
    return lp

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
#    print bg
    bg.append((i,k))
#    print bg
    bg.append((j,l))
    
    return bg


import numpy as np
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


assert two_break_on_genome([[1,-2,-4,3]],1, 6, 3, 8) == [[1, -2], [-4, 3]]
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


fname = 'rosalind_ba6k.txt'
with open(fname, "r") as f:
    p = f.readlines()
genome = p[0].strip()
nums = p[1]
i,j,k,l = map(int,nums.split(', '))

#genome = '(+1 -2 -3 +4 -5 +6 +7 -8 +9 +10 +11 -12 +13 -14 -15 +16 -17 -18 +19 -20 +21 +22 -23 -24 +25 -26 -27 -28 -29 -30 +31 -32 +33 -34 -35 +36 +37 -38 -39 +40 +41 +42 -43 +44 +45 -46 +47 +48 +49 +50 +51 -52 +53 +54 -55 -56 -57 -58 +59 -60 -61 -62 +63)'
#i,j,k,l = 8, 10, 116, 113
genome = genome_str_to_list(genome)
genome = two_break_on_genome(genome,i,j,k,l)
fs = format_sequence(genome)
print ''.join(fs)