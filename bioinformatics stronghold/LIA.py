"""
http://rosalind.info/problems/lia/
"""

import sys
sys.path.append('../')
from rosalind_utils import *


def cum(k, n, p):
    """The probability of having at least k in n trial"""
    return sum(choose(n,i) * p**i * (1-p)**(n-i)
                for i in xrange(k, n+1))

def lia():
    k, n = map(int, open("rosalind_lia.txt").read().split())

    # the prob is always 0.25 (for all generations)

    print cum(n, 2**k, 0.25)

lia()