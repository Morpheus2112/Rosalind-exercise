# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 13:51:30 2018

@author: Memphis
"""

with open('rosalind_ba1l.txt') as input_data:
    text = input_data.readline().strip()



def trans(str):
    a = str.replace('A','0')
    b = a.replace('C','1')
    c = b.replace('G','2')
    d = c.replace('T','3')
#    print d
    num = int(d,4)
    return num


print(trans(text))