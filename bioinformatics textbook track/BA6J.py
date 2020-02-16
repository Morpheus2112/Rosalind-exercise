# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:37:22 2018

@author: palan
"""

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
    print bg
    bg.append((i,k))
    print bg
    bg.append((j,l))
    
    return bg




#g = [(1, 3), (4, 5), (6, 7), (8, 9), (10, 12), (11, 14), (13, 15), (16, 18), (17, 20), (19, 21), (22, 23), (24, 26), (25, 27), (28, 29), (30, 32), (31, 33), (34, 35), (36, 37), (38, 40), (39, 42), (41, 43), (44, 46), (45, 48), (47, 49), (50, 51), (52, 54), (53, 55), (56, 57), (58, 59), (60, 61), (62, 63), (64, 65), (66, 67), (68, 70), (69, 72), (71, 74), (73, 75), (76, 77), (78, 79), (80, 81), (82, 83), (84, 86), (85, 88), (87, 89), (90, 92), (91, 93), (94, 96), (95, 97), (98, 100), (99, 101), (102, 103), (104, 106), (105, 108), (107, 110), (109, 112), (111, 114), (113, 115), (116, 117), (118, 120), (119, 122), (121, 123), (124, 126), (125, 127), (128, 129), (130, 131), (132, 133), (134, 136), (135, 2)]
#(i,j,k,l) = (109, 112, 64, 65)

fname = 'rosalind_ba6j.txt'
with open(fname, "r") as f:
    p = f.readlines()
q = p[0].strip().split(')')
nums = p[1]
t,j,k,l = map(int,nums.split(', '))
import re
p = []
for i in q:
    p.append(re.findall(r'\d+', i))
z = []
for i in p:
    if len(i) > 1:
        z.append((int(i[0]), int(i[1])))
print two_break_on_genome_graph(z,t,j,k,l)