#!/usr/bin/env python
'''
Problem Title: Median
Rosalind ID: MED
Algorithmic Heights #: 024
URL: http://rosalind.info/problems/med/
'''

f=open("rosalind_med.txt", "r")
c=0
k=0
l=[]
for i in f.readlines():
    if c==1:
        a=i.replace("\n", "").split(" ")
        for j in a:
            l.append(int(j))
    elif c==2:
        k=i.replace("\n", "")
    c+=1
#print l
#print k
a=sorted(l)
print a[int(k)-1]