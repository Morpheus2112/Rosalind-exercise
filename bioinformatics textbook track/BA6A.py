# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:50:21 2018

@author: palan
"""
import numpy as np

def reversal(p, i, k):
    prefix = p[:i]
    suffix = p[k+1:]
    root = p[i:k+1]
    return prefix + map(lambda x: -x, root[::-1]) + suffix

def greedy_sorting(p):
    '''
    CODE CHALLENGE: Implement GREEDYSORTING.
    Input: A permutation P.
    Output: The sequence of permutations corresponding to 
    applying GREEDYSORTING to P, ending with
    the identity permutation.
    '''
    s = []
    for i in range(1,len(p)+1):
        try:
            k = p.index(-i)
            p = reversal(p,i-1,k)
            s.append(p)
        except ValueError:
            k = p.index(i)
            if (k != i-1):
                p = reversal(p,i-1,k)
                s.append(p)
                p = p[:]
                p[i-1] = -p[i-1]
                s.append(p)
    return s

def permutation_list_to_str(p):
    def str_val(i):
        if (i>0):
            return '+'+str(i)
        else:
            return str(i)
    return '(' + ' '.join(map(str_val,p)) + ')'

def permutation_str_to_list(str_p):
    p = map(int,str_p.strip()[1:-1].split(' '))
    return p
        
def format_sequence(s):
    fs = []
    for p in s:
        str_p = permutation_list_to_str(p)
        fs.append(str_p)
    return fs
    









fname = 'rosalind_ba6a.txt'
with open(fname, "r") as f:
    p = f.read()
p = p = permutation_str_to_list(p)
s = greedy_sorting(p)
fs = format_sequence(s)
with open(fname+'.out.txt', "w") as f:
    for p in fs:
        f.write(p+'\n')