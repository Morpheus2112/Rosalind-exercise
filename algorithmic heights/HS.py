# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:42:22 2017

@author: Memphis
"""

# http://rosalind.info/problems/hs

def heapify(heap, i):
    """Given a heap and recently added element at heap[i], perform up-heap
    operation to conserve the heap property"""
    if i==0:
        return
    parent = (i-1)/2
    child = i
    if heap[parent] > heap[child]:
        return
    else:
        heap[parent], heap[child] = heap[child], heap[parent]
        heapify(heap, parent)
    
def sift_down(heap, start, end):
    # sift-down the element at heap[start] to its proper place
    root = start
    while root*2+1 <= end:
        child = root*2 + 1              # left child
        swap = root                     # keeps track of child to swap with
        if heap[swap] < heap[child]:
            swap = child
        # if there is a right child and that child is greater
        if child+1 <= end and heap[swap] < heap[child+1]:
            swap = child+1
        if swap != root:
            heap[root], heap[swap] = heap[swap], heap[root]
            root = swap
        else:
            return
        
def hs():
    with open("rosalind_hs.txt") as f:
        n = int(f.readline().strip())
        A = map(int, f.readline().split())
    heap = []
    # Build the heap in array so that the largest value is at the root
    for i in range(len(A)):
        # add element to the bottom level of the heap.
        heap.append(A[i])
        # heapify
        heapify(heap, i)

    end = len(heap)-1
    while end > 0:
        # heap[0] is the root and the largest value. The swap moves it in front
        # of the sorted elements
        heap[end], heap[0] = heap[0], heap[end]
        # The heap size is reduced by one
        end = end - 1
        # The swap ruined the heap property, so restore it.
        sift_down(heap, 0, end)

    # print the sorted array
    return ' '.join(map(str, heap))
     

if __name__ == "__main__":
    s = hs()
    with open('output_hs.txt','w') as g:
        g.write(s)