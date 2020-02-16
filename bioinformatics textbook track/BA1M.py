# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 13:53:53 2018

@author: Memphis
"""

with open('rosalind_ba1m.txt') as input_data:
    index = int(input_data.readline().strip())
    k = int(input_data.readline().strip())
    
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


print(rev_trans(index,k))