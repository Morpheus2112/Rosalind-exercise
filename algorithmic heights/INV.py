# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:46:50 2017

@author: Memphis
"""

def inv():

    with open("rosalind_inv.txt") as f:
        n = int(f.readline().strip())
        list = map(int,f.readline().strip().split())
#    print n
#    print list
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if list[i] > list[j]:
                count += 1
    print count
    
    
if __name__ == "__main__":
    inv()




#
#merge_sort(list, low, high){
#  cc_inversions = 0
#  if(low < high){
#    mid = low + (high - low) / 2
#    cc_inversions = merge_sort(list, low, mid);
#    cc_inversions += merge_sort(list, mid + 1, high);
#    cc_inversions += merge(list, low, mid, high);
# }
# return cc_inversions;
#}
#
#merge(list, low, mid, high){
#  let tmp_list be of size high - low + 1;
#  ai = low, bi = mid + 1;
#  n1 = mid - ai + 1;
#  n2 = high - mid;
#  k = 0;
#  cc_inversions = 0;
#  while(ai < n1 && bi < n2){
#    if(list[ai] <= list[bi]){
#      tmp_list[k++] = list[ai++];
#    }
#    else{
#      tmp_list[k++] = list[bi++];
#      cc_inversions += (mid - ai + 1);
#    }
#  }
#  while(ai < n1){ tmp_list[k++] = list[ai++]; }
#  while(bi < n2){ tmp_list[k++] = list[bi++]; }
#  for(i = 0 to n1 + n2 - 1){
#    list[low + i] = tmp_list[i];
#  }
#  return cc_inversions;
#}







