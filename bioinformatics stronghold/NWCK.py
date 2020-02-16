# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/nwck/
"""

from math import *
import sys
sys.path.append('../')
from rosalind_utils import *

from StringIO import StringIO
from Bio import Phylo
import networkx

def nwck():
    with open("rosalind_nwck.txt") as f:
        lines = map(lambda l: l.strip(), f.readlines())
        lines = [line for line in lines if line]

    for i in xrange(len(lines)/2):
        handle = StringIO(lines[2*i])
        tree = Phylo.read(handle, "newick")
        names = lines[2*i+1].split()

        t =  Phylo.to_networkx(tree)

        na = [node for node in t.nodes() if node.name == names[0]][0]
        nb = [node for node in t.nodes() if node.name == names[1]][0]

        print len(networkx.shortest_path(t, na, nb))-1,

    print ""

nwck()