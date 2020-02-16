# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:14:15 2017

@author: Memphis
"""

f = open('rosalind_ini2.txt', 'r')
texts = f.readlines()
f.close()


a,b = (texts[0].strip('\n').split(' '))
a = int(a)
b = int(b)


print a**2 + b**2