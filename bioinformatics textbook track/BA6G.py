# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:35:23 2018

@author: palan
"""

def cycle_to_chromosome(nodes):
    '''
    CODE CHALLENGE: Implement CycleToChromosome.
    Input: A sequence Nodes of integers between 1 and 2n.
    Output: The chromosome Chromosome containing n synteny blocks resulting 
    from applying CycleToChromosome to Nodes.
    '''
    p = []
    for j in range(0,len(nodes)/2):
        if nodes[2*j] < nodes[2*j+1]:
            s = j+1
        else:
            s = -(j+1)
        p.append(s)
    return p

def permutation_str_to_list(str_p):
    p = map(int,str_p.strip()[1:-1].split(' '))
    return p

def permutation_list_to_str(p):
    def str_val(i):
        if (i>0):
            return '+'+str(i)
        else:
            return str(i)
    return '(' + ' '.join(map(str_val,p)) + ')'
fname = 'rosalind_ba6g.txt'
with open(fname, "r") as f:
    p = f.read()
p = permutation_str_to_list(p)
p = cycle_to_chromosome(p)
print permutation_list_to_str(p)