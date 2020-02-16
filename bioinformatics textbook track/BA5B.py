# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:36:14 2018

@author: palan
"""
import numpy as np
def manhattan_tourist(n, m, down, right):
    '''
    Find the length of a longest path in the Manhattan Tourist Problem.
    Input: Integers n and m, followed by an n × (m + 1) matrix Down 
    and an (n + 1) × m matrix Right.
    Output: The length of a longest path from source (0, 0) to sink 
    (n, m) in the n × m rectangular grid whose edges are defined by the 
    matrices Down and Right.
    Warning : n rows, m columns
    '''
    down = np.array(down).reshape(n, m+1)
    right = np.array(right).reshape(n+1, m)
    s = np.empty(shape = (n+1,m+1), dtype = int) 
    s[0,0] = 0
    for i in range(n):
        s[i+1,0] = s[i,0] + down[i,0]
    for j in range(m):
        s[0,j+1] = s[0,j] + right[0,j]
    for i in range(n):
        for j in range(m):
            s[i+1,j+1] = max(s[i,j+1]+down[i,j+1], s[i+1,j]+right[i+1,j])
#            print 's[',i+1,j+1,']=max',s[i,j+1],'+',down[i,j+1],',',s[i+1,j],'+',right[i+1,j]
    return s[n,m]

fname = 'rosalind_ba5b.txt'
lines = list(l.strip() for l in open(fname))
n = int(lines[0].split(' ')[0])
m = int(lines[0].split(' ')[1])
down = map(lambda l : map(int, l.split(' ')), lines[1:1+n])
assert lines[1+n] == '-'
right = map(lambda l : map(int, l.split(' ')), lines[2+n:2+n+n+1])
print manhattan_tourist(n, m, down, right)