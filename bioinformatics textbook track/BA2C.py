# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 16:11:34 2018

@author: Memphis
"""

with open('rosalind_ba2c.txt') as input_data:
    text = input_data.readline().strip()
    k = int(input_data.readline().strip())
    profile = [map(float, i.strip().split(' ')) for i in input_data.readlines()]

def trans(str):
    a = str.replace('A','0')
    b = a.replace('C','1')
    c = b.replace('G','2')
    d = c.replace('T','3')
#    print d
    num = int(d,4)
    
    return num

def rev_trans(index, k):
    st = ''
    for i in range(k):
        rem = index % 4
        st = str(rem)+ st
        index = index // 4
    
    a = st.replace('0','A')
    b = a.replace('1','C')
    c = b.replace('2','G')
    d = c.replace('3','T')
    return d

def ProfileProbable(text,k, profile):
    probs = [0] * 4**k
    for i in range(len(text)-k+1):
        prob = 1
        pattern = text[i:i+k]
        for j in range(k):
            prob *= profile[trans(pattern[j])][j]
        probs[trans(pattern)] = prob
    m = max(probs)
    for x in range(4**k):
        if probs[x] == m:
            return rev_trans(x,k)
        
print(ProfileProbable(text,k,profile))