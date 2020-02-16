# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 00:19:10 2017

@author: Memphis
"""

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)


if __name__ == "__main__":
    with open("rosalind_ms.txt") as f:
        n = int(f.readline().split()[0]) # number of arrays
        l = map(int, f.readline().split())
        res = mergesort(l)
        s =  ' '.join(map(str, res))
    with open('output_ms.txt','w') as g:
        g.write(s)