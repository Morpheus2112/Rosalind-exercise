# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 13:31:59 2018

@author: Memphis
"""


with open('rosalind_ba1k.txt') as input_data:
    text = input_data.readline().strip()
    k = int(input_data.readline().strip())
    

kmers = [0] * 4**k

def trans(str):
    a = str.replace('A','0')
    b = a.replace('C','1')
    c = b.replace('G','2')
    d = c.replace('T','3')
#    print d
    num = int(d,4)
    
    return num
for i in range(len(text)-k+1):
    kmers[trans(text[i:i+k])] += 1
    
print(' '.join(map(str,kmers)))