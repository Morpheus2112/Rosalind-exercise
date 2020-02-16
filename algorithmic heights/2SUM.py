# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:54:43 2017

@author: Memphis
"""
f = open('rosalind_2sum.txt', 'r')
texts = f.readlines()
f.close()


lists = texts[1:]


#def twosum(a):
#    record = -1
#    for i in range(len(a)-1):
#        for j in range(i+1,len(a)):
#            if a[i] + a[j] == 0:
#                record = [i+1,j+1]
#    return record


def twosum(a):
    t = max(max(a), -min(a))
    print t
    h = dict()
    for i in range(-t,t+1):
        h[i] = []
    for i in range(len(a)):
        h[a[i]].append(i)
    for i in range(len(a)):
        other = -a[i]
        if len(h[other]) > 0 :
            if other == a[i] and len(h[other]) >1:
                return [h[other][0]+1, h[other][1]+1]
            elif other != a[i]:
                return [i+1, h[other][0]+1]
    return -1
      
            






rt = []    
for list in lists:
    a = [int(i) for i in list.strip('\n').split(' ')]
    print twosum(a)
    rt.append(twosum(a))
    
g = open('output_2sum.txt', 'w')
for i in xrange(len(rt)):
    if rt[i] == -1:
        g.write('-1\n')
    else:
        g.write(str(rt[i][0])+' '+str(rt[i][1])+'\n')
g.close()