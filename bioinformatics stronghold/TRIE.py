# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/trie/
"""

import sys
sys.path.append('../')
from rosalind_utils import *
import Queue

num_nodes = 0
class Node:
    def __init__(self):
        global num_nodes
        self.id = num_nodes+1
        num_nodes += 1
        self.edges = {}

def trie():
    seqs = [line.strip() for line in open("rosalind_trie.txt").readlines()]
    seqs.sort(key=lambda x: len(x), reverse=True)

    # create root node
    root = Node()
    for seq in seqs:
        cur_node = root
        for c in seq:
            if c not in cur_node.edges:
                new_node = Node()
                cur_node.edges[c] = new_node
            cur_node = cur_node.edges[c]

    # print all the tree (guaranteed to be acyclic)
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        cur_node = q.get()
        for let in cur_node.edges:
            print "%d %d %c" % (cur_node.id, cur_node.edges[let].id, let)
            q.put(cur_node.edges[let])

trie()