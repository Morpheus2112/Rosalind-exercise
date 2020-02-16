# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:36:57 2018

@author: Memphis
"""

def spectral_alignment(seq, spectrum, threshold):
    spectrum.insert(0,0)    
    score = dict((i,dict((j,[-100000.0]*len(spectrum)) for j in xrange(weight(seq)+1) )) for i in xrange(0, threshold+1))
    score[0][0][0] = 0
    for i in xrange(1,len(seq)+1):
        for j in xrange(len(spectrum)):
            for k in xrange(threshold+1):
                if k==0 and weight(seq[:i])-mass[seq[i-1]]>=0 and j-mass[seq[i-1]]>=0:
                    score[k][weight(seq[:i])][j] = spectrum[j]+score[k][weight(seq[:i])-mass[seq[i-1]]][j-mass[seq[i-1]]]
                elif k>0 and weight(seq[:i])-mass[seq[i-1]]>=0 and j-mass[seq[i-1]]>=0:
                    score[k][weight(seq[:i])][j] = spectrum[j]+max(score[k][weight(seq[:i])-mass[seq[i-1]]][j-mass[seq[i-1]]],
                                                       max(score[k-1][weight(seq[:i])-mass[seq[i-1]]][:j]))

                elif k>0 and weight(seq[:i])-mass[seq[i-1]]>=0 and j>0:
                    score[k][weight(seq[:i])][j] = spectrum[j]+max(score[k-1][weight(seq[:i])-mass[seq[i-1]]][:j])

    #####  trace back the path
    res = ''
    max_score = 0
    layer = 0
    col = len(spectrum)-1
    for i in xrange(threshold+1):
        if score[i][weight(seq)][len(spectrum)-1]>max_score:
            max_score = score[i][weight(seq)][len(spectrum)-1]
            layer = i
    print max_score ,i 
    for i in range(len(seq), 0, -1):
        if col-mass[seq[i-1]]>=0 and score[layer][weight(seq[:i])][col] == spectrum[col]+score[layer][weight(seq[:i])-mass[seq[i-1]]][col-mass[seq[i-1]]]:
#            layer -= 1
            col = col-mass[seq[i-1]]
            res = seq[i-1]+res
            
            
            
        elif score[layer][weight(seq[:i])][col] == spectrum[col]+max(score[layer-1][weight(seq[:i])-mass[seq[i-1]]][:col]):
            part = col-score[layer-1][weight(seq[:i])-mass[seq[i-1]]][:col].index((max(score[layer-1][weight(seq[:i])-mass[seq[i-1]]][:col])))-mass[seq[i-1]]
            col = score[layer-1][weight(seq[:i])-mass[seq[i-1]]][:col].index((max(score[layer-1][weight(seq[:i])-mass[seq[i-1]]][:col])))
            if part>0:
                res = seq[i-1]+'(+'+str(part) + ')' + res
            else:
                res = seq[i-1]+'('+str(part) + ')' + res
            layer -= 1


    return res 


def weight(seq):
    total = 0
    for i in seq:
        total += mass[i]
    return total



mass = {'G':57,
        'A':71,
        'S':87,
        'P':97,
        'V':99,
        'T':101,
        'C':103,
        'I':113,
        'L':113,
        'N':114,
        'D':115,
        'K':128,
        'Q':128,
        'E':129,
        'M':131,
        'H':137,
        'F':147,
        'R':156,
        'Y':163,
        'W':186,
        'X':4,
        'Z':5}




f = open('rosalind_ba11j.txt', 'r')
lines = f.readlines()
seq = lines[0].strip()
spectrum = [int(x) for x in lines[1].strip().split()]
threshold = int(lines[2])
print spectral_alignment(seq, spectrum, threshold)