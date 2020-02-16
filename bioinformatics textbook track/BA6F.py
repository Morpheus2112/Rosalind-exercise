# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:31:32 2018

@author: palan
"""

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

fname = 'rosalind_ba6f.txt'
with open(fname, "r") as f:
    p = f.read()
p = permutation_str_to_list(p)
p = chromosome_to_cycle(p)
print '('+' '.join(map(str,p))+")"