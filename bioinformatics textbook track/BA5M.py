# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:18:16 2018

@author: palan
"""

def multiple_alignment_3(v, w, u):
    '''Returns the alignment of three sequences v, w, and u.'''
    # Initialize the matrices.
    S = [[[0 for k in xrange(len(u)+1)] for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[[0 for k in xrange(len(u)+1)] for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            for k in xrange(1, len(u)+1):
                scores = [S[i-1][j-1][k-1] + int(v[i-1] == w[j-1] == u[k-1]), S[i-1][j][k], S[i][j-1][k], S[i][j][k-1], S[i-1][j][k-1], S[i][j-1][k-1]]
                backtrack[i][j][k], S[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    v_aligned, w_aligned, u_aligned = v, w, u

    # Get the position of the highest scoring cell in the matrix and the high score.
    i, j, k = len(v), len(w), len(u)
    max_score = S[i][j][k]

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j*k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
            u_aligned = insert_indel(u_aligned, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
            u_aligned = insert_indel(u_aligned, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            v_aligned = insert_indel(v_aligned, i)
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            u_aligned = insert_indel(u_aligned, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    # Prepend the necessary preceeding indels to get match lengths.
    while len(v_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        v_aligned = insert_indel(v_aligned, 0)
    while len(w_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        w_aligned = insert_indel(w_aligned, 0)
    while len(u_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        u_aligned = insert_indel(u_aligned, 0)

    return str(max_score), v_aligned, w_aligned, u_aligned



#v = 'ATATCCG'
#w = 'TCCGA'
#u = 'ATGTACTG'
    
fname = 'rosalind_ba5m.txt'
lines = list(l.strip() for l in open(fname))
v = lines[0].strip()
w = lines[1].strip()
u = lines[2].strip()

(a,b,c,d) = multiple_alignment_3(v,w,u)
print int(a)
print b
print c
print d