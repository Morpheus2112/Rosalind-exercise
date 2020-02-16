# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:11:07 2018

@author: palan
"""

def tree_coloring(edge_lines,node_lines):
    """
    Tree Coloring Problem: Color the internal nodes of a tree given the colors of its leaves.
    Input: An adjacency list, followed by color labels for leaf nodes.
    0 -> {}
    1 -> {}
    2 -> 0,1
    3 -> {}
    4 -> {}
    5 -> 3,2
    6 -> {}
    7 -> 4,5,6
    -
    0: red
    1: red
    3: blue
    4: blue
    6: red    
    Output : Color labels for all nodes, in any order.
    0: red
    1: red
    2: red
    3: blue
    4: blue
    5: purple
    6: red
    7: purple    
    """
    tree_adjlist = [None]*(len(edge_lines))
    tree_color = {}
    for l in edge_lines:
        # parse edge parent node
        spl = l.strip().split(' -> ')
        parent_id = int(spl[0])
        if spl[1] != '{}':
            # (let leaves None as initialized)
            # parse edge children node
            children_ids = [int(c) for c in spl[1].split(',')]
            tree_adjlist[parent_id] = children_ids
    for l in node_lines:
        # parse node id
        spl = l.strip().split(': ')
        node_id = int(spl[0])
        if spl[1] == 'red':
            tree_color[node_id] = 1
        elif spl[1] == 'blue':
            tree_color[node_id] = 2
        else:
            print 'weird color (',spl[1],') here, shall not happen'
    def color_node(current_id):
        if current_id in tree_color.keys():
            return tree_color[current_id]
        current_list = tree_adjlist[current_id]
        assert current_list is not None
        color = 0
        for child_id in current_list:
            if child_id in tree_color.keys():
                color |= tree_color[child_id]
            else:
                color |= color_node(child_id)
        tree_color[current_id] = color
        return color
    map(color_node,range(len(tree_adjlist)))
    def colored_node_tostr(k,v):
        if v == 1:
            return str(k)+': red'
        elif v == 2:
            return str(k)+': blue'
        elif v == 3:
            return str(k)+': purple'
        else:
            print 'weird color value (',str(c),') here, shall not happen'
            
    color_list = sorted([colored_node_tostr(k,v) for k,v in tree_color.iteritems()])
    return '\n'.join(color_list)  


fname = 'rosalind_ba9p.txt'
with open(fname, "r") as f:
    l = f.read().splitlines()
    i = l.index('-')
    edge_lines = l[:i]
    node_lines = l[i+1:]
s = tree_coloring(edge_lines,node_lines)
with open(fname+'.out.txt', "w") as f:
    f.write(s)