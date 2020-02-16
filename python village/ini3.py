# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 23:41:24 2017

@author: Memphis
"""

f = open('rosalind_ini3.txt', 'r')
texts = f.readlines()
f.close()

text = texts[0].strip('\n')
nums = [int(i) for i in texts[1].strip('\n').split(' ')]

a1 = nums[0]
a2 = nums[1]
b1 = nums[2]
b2 = nums[3]

print(text[a1:a2+1])
print(text[b1:b2+1])