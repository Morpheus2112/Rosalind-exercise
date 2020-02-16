# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:00:06 2018

@author: palan
"""
def permutation_str_to_list(str_p):
    p = map(int,str_p.strip()[1:-1].split(' '))
    return p

def number_of_breakpoints(p):
        '''
        CODE CHALLENGE: Solve the Number of Breakpoints Problem.
        
        Number of Breakpoints Problem: Find the number of breakpoints in a permutation.
        Input: A permutation.
        Output: The number of breakpoints in this permutation.        
        '''
        adj = 0
        p = [0,] + p + [len(p)+1]
        for i in range(0,len(p)-1):
            if (p[i+1]==p[i]+1):
                adj += 1
        return len(p) - 1 - adj






fname = 'rosalind_ba6b.txt'
with open(fname, "r") as f:
    p = f.read()
p = permutation_str_to_list(p)
print number_of_breakpoints(p)