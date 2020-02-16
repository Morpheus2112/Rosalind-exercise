# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:40:28 2018

@author: palan
"""
def chromosome_to_cycle(p):
    '''
    CODE CHALLENGE: Implement ChromosomeToCycle.
    Input: A chromosome Chromosome containing n synteny blocks.
    Output: The sequence Nodes of integers between 1 and 2n resulting 
    from applying ChromosomeToCycle to Chromosome.
    '''
    nodes = []
    
    for i in p:
        if (i>0):
            nodes.append(2*i-1)
            nodes.append(2*i)
        else:
            nodes.append(-2*i)
            nodes.append(-2*i-1)
    return nodes

def permutation_str_to_list(str_p):
    p = map(int,str_p.strip()[1:-1].split(' '))
    return p

def colored_edges(genome):
    '''
    CODE CHALLENGE: Implement ColoredEdges.
    Input: A genome P.
    Output: The collection of colored edges in the genome graph of P 
    in the form (x, y).
    '''
    g = []
    for p in genome:
        s = chromosome_to_cycle(p)
        for j in range(len(s)/2):
            head = 1+2*j
            tail = (2+2*j) % len(s)
            e = (s[head],s[tail])
            g.append(e)
    return g

def genome_str_to_list(genome):
    lp = []
    for p in genome.split('(')[1:]:
        p = permutation_str_to_list( '(' + p )
        lp.append(p)
    return lp


genome = '(-1 +2 -3 -4 -5 +6 -7 +8 +9 +10 +11 -12 +13 -14 -15 +16 +17 -18 -19 +20 +21 +22 +23 -24 +25 -26 -27 -28 +29 -30 -31)(-32 +33 -34 -35 -36 +37 -38 +39 -40 +41 +42 -43 +44 -45 -46 -47 +48 -49 +50 -51 +52 -53 +54)(-55 -56 +57 +58 +59 +60 -61 -62 +63 -64 -65 -66 -67 +68 -69 +70 -71 +72 -73 +74 -75 +76 -77 +78 +79 +80 -81)(-82 -83 +84 -85 -86 +87 -88 -89 +90 +91 +92 +93 -94 -95 +96 -97 -98 +99 -100 -101 +102 +103 +104 +105 +106 -107 -108 +109 +110 -111)(-112 +113 +114 -115 -116 +117 +118 -119 -120 -121 +122 +123 -124 -125 +126 -127 +128 +129 -130 -131 -132 +133 -134 -135)(-136 -137 +138 -139 -140 -141 +142 -143 -144 -145 -146 -147 +148 +149 +150 +151 +152 +153 -154 -155 -156 -157 -158 +159 -160 -161)(+162 +163 -164 -165 -166 +167 +168 +169 -170 -171 -172 -173 +174 +175 +176 +177 +178 -179 -180 +181 +182 -183 -184)(+185 -186 -187 +188 +189 +190 -191 -192 +193 -194 -195 +196 -197 +198 +199 -200 -201 -202 -203 +204 -205 +206)'
genome = '(+1 -2 -3)(+4 +5 -6)'

fname = 'rosalind_ba6h.txt'
with open(fname, "r") as f:
    p = f.read()
genome = genome_str_to_list(p)
col = colored_edges(genome)
print ', '.join(map(str,col)) 


