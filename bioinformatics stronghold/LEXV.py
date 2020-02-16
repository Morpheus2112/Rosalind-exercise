# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/lexv/
"""

import sys
sys.path.append('../')
import rosalind_utils

def lexv_helper(lets, cur_str, max_len):
    if len(cur_str) > max_len:
        return
    print cur_str
    for i in xrange(len(lets)):
        lexv_helper(lets, cur_str + lets[i], max_len)

def lexv():
    lines = open("rosalind_lexv.txt").readlines()
    lets = lines[0].split()
    max_len = int(lines[1])
    lexv_helper(lets, "", max_len)

lexv()