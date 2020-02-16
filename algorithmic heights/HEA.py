# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 00:51:02 2017

@author: Memphis
"""

# http://rosalind.info/problems/hea/
import math

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
    
def hs():
    with open("rosalind_hea.txt") as f:
        n = int(f.readline().strip())
        A = map(int, f.readline().split())
    heap = []
    # build heap here
    for i in range(len(A)):
        # add element to the bottom level of the heap.
        heap.append(A[i])
        # heapify
        heapify(heap, i)
    # print heap
    return ' '.join(map(str, heap))

if __name__ == "__main__":
    a  = hs()
    with open('output_hea.txt','w') as g:
        g.write(a)

#
#
#  return node != 0 ? (node - 1) / 2 : 0;
#}
#
#left(node){
#  return (2 * node + 1);
#}
#
#right(node){
#  return (2 * node + 2);
#}
#
#heapify(list, node){
#  rightnode = right(node), leftnode = left(node), largest = node;
#  if(leftnode < list.length && list[leftnode] > list[largest])
#    largest = leftnode;
#  if(rightnode < list.length && list[rightnode] > list[largest])
#    largest = rightnode;
#  if(largest != node){
#    swap(list[largest], list[node]);
#   heapify(list, largest);
# }
#}
#
#max_heap(list){
#  for(i = list.length / 2 to 0)
#    heapify(list, i);
#}