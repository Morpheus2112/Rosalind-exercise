# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 23:45:49 2017

@author: Memphis
"""

f = open('rosalind_ini4.txt', 'r')
texts = f.readlines()
f.close()

nums = [int(i) for i in texts[0].strip('\n').split(' ')]
a = nums[0] 
b = nums[1]

i = a
sum = 0
while a <= b:
    if a % 2 == 1:
        sum  = sum + a
    a = a + 1
    
print sum