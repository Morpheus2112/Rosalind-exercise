# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 10:01:37 2018

@author: Memphis
"""

inf = 1000000000 # large number as Inf
def Bellman_Ford(edgelist,nodenum,start = 0):
    # init
    dist = [inf for i in range(nodenum)]
    dist[start] = 0
    for n in range(len(edgelist)):
        if edgelist[n][0] == start:
            dist[edgelist[n][1]] = edgelist[n][2]

    for m in range(nodenum-1):
        check = 0
        for n in range(len(edgelist)):
            # relax
            if(dist[edgelist[n][1]-1]>dist[edgelist[n][0]-1]+edgelist[n][2] and dist[edgelist[n][0]-1]!=inf):
                dist[edgelist[n][1]-1] = dist[edgelist[n][0]-1] + edgelist[n][2]
                check = 1

    flag = 0
    #  has the the circle of edge<0?
    for n in range(len(edgelist)):
        if (dist[edgelist[n][1]-1] > dist[edgelist[n][0]-1] + edgelist[n][2]):
            flag = 1
            break
        if flag == 1:
            return None
    return dist

with open('rosalind_sdag.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            nodenum = int(line.rstrip().split()[0])
            edgelist = [] # start,end,weight

        else:
            temp = line.rstrip().split()
            start = int(temp[0])
            end = int(temp[1])
            length = int(temp[2])
            for k in range(len(edgelist)):  # bug: same edge,different length ,must use the last edge
                if edgelist[k][0]==start and edgelist[k][1]==end:
                    edgelist.pop(k)
                    break
            edgelist.append([start,end,length])


# bug: the right answer must include a space at the end of answer
for x in Bellman_Ford(edgelist,nodenum,0):
    if x > inf / 10:
        print 'x',
    else:
        print str(x), 