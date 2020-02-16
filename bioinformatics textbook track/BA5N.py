# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:32:52 2018

@author: palan
"""
import copy



class edge_weighted_graph:
    def __init__(self):
        # set of vertex
        self.vertex = set()
        # adjacency list of set of edge : 
        # key = vertex initial
        # value = ( ..., (vertex final, distance), ...)
        self.edge = {}
        return
        
    def add_edge(self, u, v, w):
        '''
        add a weigthed edge from vertex u to v
        '''
        assert u != v
        self.vertex.add(u)
        self.vertex.add(v)
        self.edge.setdefault(u,set()).add((v,w))
    
    def remove_edge(self, u, v, w):
        '''
        remove a weighted edge from vertex u to v
        '''
        assert u != v
        d = self.edge.get(u, set())
        d.remove((v, w))
    
    def sub_graph(self, u):
        '''
        return the sub graph starting from vertex u
        '''
        sg = edge_weighted_graph()
        on_stack = []
        on_stack.append(u)
        while (on_stack):
            u = on_stack.pop()
            for (v,w) in self.edge.get(u, set()):
                sg.add_edge(u, v, w)
                on_stack.append(v)
        return sg
    
    def reverse(self):
        '''
        return the reversed graph
        '''
        r = edge_weighted_graph()
        for u,d in self.edge.iteritems():
            for (v,w) in d:
                r.add_edge(v, u, w)
        return r
    
    def sort(self):
        '''
        return a topologically sorted list of vertex
        '''
        s = []
        g = copy.deepcopy(self)
        r = g.reverse()
        candidates = [ u for u in self.vertex if not r.edge.get(u, set())]
        while candidates:
            u = candidates.pop()
#            print '---------'
#            print 'u=',u
#            print 'g.edge',g.edge
#            print 'r.edge',r.edge
            s.append(u)
            for (v,w) in set(g.edge.get(u, set())):
                # remove u->v edge from g and u-> from r
                g.remove_edge(u, v, w)
                r.remove_edge(v, u, w)
                if not r.edge[v]:
                    r.edge.pop(v, None)
                    candidates.append(v)
            g.edge.pop(u, None)
        assert not g.edge
        assert not r.edge
        return s
    
    def __str__(self):
        s = ''
        for u,d in self.edge.iteritems():
            for (v,w) in d:
                 s += str(u) + '->' + str(v) + ':' + str(w) + '\n'
        return s


fname = 'rosalind_ba5n.txt'
lines = list(l.strip() for l in open(fname))
d = []
for l in lines:
    a ,b= l.split('->')
    c  = b.split(",")
    for i in c:
        d.append(( int(a), int(i),1))

edges = d[:]

g = edge_weighted_graph()
for (u,v,w) in edges:
    g.add_edge(u, v,w)

print g.sort()