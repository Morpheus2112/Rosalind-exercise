# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:53:24 2017

@author: Memphis
"""

f = open('rosalind_maj.txt', 'r')
texts = f.readlines()
f.close()

num =  [int(i) for i in texts[0].strip('\n').split(' ')]
lists = texts[1:]

def MajorElement(a):
    count = 0
    for i in range(0,len(a)):
        if count == 0:
            major = a[i]
        if a[i] == major:
            count += 1
        else:
            count -= 1
    count = 0
    for i in range(0,len(a)):
        if a[i] == major:
            count += 1
    if count > len(a)//2:
        return major
    else:
        return -1
        
for list in lists:
    a  = [int(i) for i in list.strip('\n').split(' ')]
    print MajorElement(a),