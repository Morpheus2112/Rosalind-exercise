# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:58:40 2017

@author: Memphis
"""

def three_sum(xs):
    original_xs = xs[:]
    xs.sort()
    n = len(xs)
    for i in xrange(n-2):
        a = xs[i]
        j = i+1
        k = n-1
        while j < k:
            b = xs[j]
            c = xs[k]
            if a+b+c == 0:
                return sorted([original_xs.index(a)+1,
                               original_xs.index(b)+1,
                               original_xs.index(c)+1])
            elif a+b+c > 0:
                k = k-1
            else:
                j = j+1
    return [-1]




if __name__ == "__main__":
    with open("rosalind_3sum.txt") as f:
        k = int(f.readline().split()[0]) # number of arrays
        for i in xrange(k):
            xs = map(int, f.readline().split())
            res = three_sum(xs)
            print ' '.join(map(str, res))