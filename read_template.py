# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:28:11 2017

@author: Memphis
"""

f = open('rosalind_ini3.txt', 'r')
texts = f.readlines()
f.close()

text = texts[0].strip('\n')
nums = [int(i) for i in texts[1].strip('\n').split(' ')]




g = open('output_ini5.txt', 'w')
for i in xrange(len(texts)):
    if i % 2 == 1:
        g.write(texts[i])
g.close()




if __name__ == "__main__":
    with open("rosalind_ms.txt") as f:
        n = int(f.readline().split()[0]) # number of arrays
        l = map(int, f.readline().split())
        res = mergesort(l)
        s =  ' '.join(map(str, res))
    with open('output_ms.txt','w') as g:
        g.write(s)