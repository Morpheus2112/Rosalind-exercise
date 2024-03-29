# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:47:36 2018

@author: palan
"""
import numpy as np
def graph_to_genome(g):
    '''
    CODE CHALLENGE: Implement GraphToGenome.
    Input: The colored edges ColoredEdges of a genome graph.
    Output: The genome P corresponding to this genome graph.
    '''
    
    genome = []
    visit = []
    adj = np.zeros(len(g)*2, dtype = np.int)
    for t in g:
        adj[t[0]-1] = t[1]-1
        adj[t[1]-1] = t[0]-1
    
    for t in g:
        orig = t[0]
        if orig in visit:
            continue
        visit.append(orig)
        if (orig%2 == 0):
            closing = orig-1
        else:
            closing = orig+1
        p = []
        i = 0
        while(True):
            if (orig%2 == 0):
                p.append(orig/2)
            else:
                p.append(-(orig+1)/2)
            dest = adj[orig-1]+1
            i = i + 1
            if (i>100):
                assert False
                return
            visit.append(dest)
            if (dest == closing):
                genome.append(p)
                break
            if (dest%2 == 0):
                orig = dest -1
            else:
                orig = dest + 1
            assert orig > 0
            visit.append(orig)
    return genome


def format_sequence(s):
    fs = []
    for p in s:
        str_p = permutation_list_to_str(p)
        fs.append(str_p)
    return fs

def permutation_list_to_str(p):
    def str_val(i):
        if (i>0):
            return '+'+str(i)
        else:
            return str(i)
    return '(' + ' '.join(map(str_val,p)) + ')'



g = [(1, 4), (3, 6), (5, 7), (8, 9), (10, 11), (12, 14), (13, 16), (15, 18), (17, 20), (19, 22), (21, 23), (24, 25), (26, 28), (27, 30), (29, 32), (31, 34), (33, 35), (36, 38), (37, 40), (39, 41), (42, 44), (43, 46), (45, 48), (47, 49), (50, 2), (52, 53), (54, 56), (55, 57), (58, 60), (59, 61), (62, 63), (64, 65), (66, 67), (68, 69), (70, 72), (71, 74), (73, 76), (75, 77), (78, 79), (80, 82), (81, 83), (84, 85), (86, 88), (87, 90), (89, 51), (91, 93), (94, 96), (95, 97), (98, 100), (99, 101), (102, 103), (104, 106), (105, 108), (107, 109), (110, 112), (111, 114), (113, 115), (116, 117), (118, 120), (119, 122), (121, 124), (123, 126), (125, 128), (127, 130), (129, 92), (131, 134), (133, 136), (135, 138), (137, 140), (139, 142), (141, 144), (143, 145), (146, 148), (147, 149), (150, 152), (151, 153), (154, 155), (156, 158), (157, 160), (159, 161), (162, 163), (164, 166), (165, 168), (167, 169), (170, 172), (171, 174), (173, 175), (176, 178), (177, 179), (180, 182), (181, 184), (183, 185), (186, 188), (187, 132), (189, 192), (191, 193), (194, 196), (195, 197), (198, 199), (200, 201), (202, 203), (204, 206), (205, 208), (207, 210), (209, 212), (211, 214), (213, 215), (216, 217), (218, 220), (219, 222), (221, 224), (223, 226), (225, 227), (228, 229), (230, 232), (231, 233), (234, 190), (235, 237), (238, 239), (240, 242), (241, 244), (243, 246), (245, 248), (247, 250), (249, 252), (251, 253), (254, 255), (256, 258), (257, 260), (259, 262), (261, 263), (264, 265), (266, 268), (267, 269), (270, 271), (272, 273), (274, 275), (276, 277), (278, 280), (279, 281), (282, 284), (283, 286), (285, 287), (288, 289), (290, 292), (291, 293), (294, 236), (296, 297), (298, 300), (299, 302), (301, 304), (303, 306), (305, 307), (308, 309), (310, 311), (312, 314), (313, 315), (316, 318), (317, 319), (320, 321), (322, 324), (323, 325), (326, 327), (328, 329), (330, 332), (331, 334), (333, 336), (335, 337), (338, 340), (339, 342), (341, 344), (343, 346), (345, 348), (347, 349), (350, 352), (351, 295), (354, 356), (355, 357), (358, 360), (359, 361), (362, 363), (364, 366), (365, 368), (367, 370), (369, 371), (372, 374), (373, 375), (376, 377), (378, 379), (380, 382), (381, 384), (383, 385), (386, 388), (387, 389), (390, 391), (392, 393), (394, 353), (396, 397), (398, 399), (400, 402), (401, 404), (403, 405), (406, 407), (408, 409), (410, 411), (412, 414), (413, 416), (415, 418), (417, 419), (420, 421), (422, 424), (423, 425), (426, 428), (427, 429), (430, 431), (432, 434), (433, 435), (436, 437), (438, 440), (439, 442), (441, 443), (444, 446), (445, 447), (448, 449), (450, 452), (451, 453), (454, 395)]
fname = 'rosalind_ba6i.txt'
with open(fname, "r") as f:
    p = f.read()
q = p.strip().split(')')
    
import re
p = []
for i in q:
    p.append(re.findall(r'\d+', i))
z = []
for i in p:
    if len(i) > 1:
        z.append((int(i[0]), int(i[1])))
genome = graph_to_genome(z)
print ''.join(format_sequence(genome))