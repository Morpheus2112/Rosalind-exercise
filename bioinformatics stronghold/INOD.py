
# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/inod/
Problem: Find the number of internal nodes of any unrooted tree having n leaves.
Solution: Let m be the number of internal nodes. In an unrooted tree, all leaves
have a degree of 1 and all internal nodes have a degree of 3. Therefore, the
total number of edges should be (n + 3m) / 2. Also, the number of edges in a
tree with (n+m) nodes should be (n+m-1).
(n + 3m) / 2 = n + m - 1
==> n + 3m = 2n + 2m - 2
==> m = n - 2
"""


def inod():
    n = int(open("rosalind_inod.txt").read())
    return n - 2

print inod()