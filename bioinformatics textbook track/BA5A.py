# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:15:24 2018

@author: palan
"""

def dynamic_programming_change(money, coins):
    '''
    CODE CHALLENGE: Solve the Change Problem.
    Input: An integer money and an array coins = (coin1, ..., coind).
    Output: The minimum number of coins with denominations coins that changes money.
    '''
    min_num_coins = []
    min_num_coins.append(0)
    for m in range (1,money+1):
        min_num_coins.append(float("inf"))
        for i in coins:
            if (m >= i):
                if min_num_coins[m - i] +  1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - i] +  1
    return min_num_coins[money]

fname = 'rosalind_ba5a.txt'
lines = list(l for l in open(fname))
p = int(lines[0].strip())
s = map(int, lines[1].strip().split(","))
print dynamic_programming_change(p,s)
        