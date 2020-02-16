# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 01:06:44 2017

@author: Memphis
"""

def par():
    with open("rosalind_par3.txt") as f:
        n = int(f.readline().strip())
        A = map(int, f.readline().split())
    B = [A[0],]
    C = []
    D = []
    for i in range(1,len(A)):
        if A[i] > A[0]:
            D.append(A[i])
        elif A[i] == A[0]:
            B.append(A[i])
        else:
            C.append(A[i])
    S = C + B + D
    return ' '.join(map(str, S))
    
if __name__ == "__main__":
    a  = par()
    with open('output_par3.txt','w') as g:
        g.write(a)


#  # we work with a zero based index of list      
#   two_way_parition(list) 
#      index, position, aperture = -1, -1, list.first # INITIALIZATION
#      while index < list.length - 1:                 # ITERATION:                  
#        index++                                      # linear lookahead
#        if list[index] <= aperture:                  # event: lookahead item is small enough to pass
#          swap(list[index], list[position+1])        # swap with big item immediately in front of mesh
#          position++                                 # pull the mesh forward
#      swap(list.first, list[position])               # FINALIZATION: first item to final position