#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Reversal Distance
Rosalind ID: REAR
Rosalind #: 042
URL: http://rosalind.info/problems/rear/
'''


def breakpoint_count(permutation):
    '''Returns the number of breakpoints in a given permutation.'''

    # Prepend 0 and append len(permutation)+1 to check if the endpoints are in place.
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return sum(map(lambda x, y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def breakpoint_indices(permutation):
    '''Returns the indices of all breakpoints in a given permutation.'''
    from itertools import compress
    # Prepend 0 and append len(permutation)+1 to check if the endpoints are in place.
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return compress(xrange(len(permutation)-1), map(lambda x, y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def greedy_breakpoint_bfs(perm1, perm2):
    '''Performs a greedy breakpoint reduction based BFS sorting of a given permutation.'''
    from itertools import product

    # Normalize the permutations so that we sort to the identity permutation (1,2,3, ..., n).
    to_identity = {value: i + 1 for i, value in enumerate(perm2)}
    normalized_perm = [to_identity[value] for value in perm1]

    # Quick lambda function to reverse a region in the permutation.
    rev_perm = lambda perm, i, j: perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]

    # Initialize Variables
    normalized_perm = tuple(normalized_perm)
    current_perms = [normalized_perm]
    min_breaks = breakpoint_count(normalized_perm)
    dist = 0

    # Run the greedy BFS breakpoint reduction sorting.
    while True:
        new_perms = []
        dist += 1
        # Iterate over all combinations of breakpoint indices for all  current minimal permutations.
        for perm in current_perms:
            for rev_ind in product(breakpoint_indices(perm), repeat=2):
                # Store some temporary variables for the given iteration.
                temp_perm = tuple(rev_perm(perm, rev_ind[0], rev_ind[1] - 1))
                temp_breaks = breakpoint_count(temp_perm)

                # Done we have no breakpoints.
                if temp_breaks == 0:
                    return dist

                # Create a new dictionary and update the minimum number of breakpoints if we've found a reduction.
                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = [temp_perm]

                # Add to the dictionary if the current breakpoints match the minimum number.
                elif temp_breaks == min_breaks:
                    new_perms.append(temp_perm)

        current_perms = new_perms


if __name__ == '__main__':

    # Read the input data.
    with open('rosalind_rear.txt') as input_data:
        permutations_list = [pair.strip().split('\n') for pair in input_data.read().split('\n\n')]
        for index, pair in enumerate(permutations_list):
            permutations_list[index] = [map(int, perm.split()) for perm in pair]

    # Get the reversal distances.
    # Apply both permutation orders since, although unlikely, sometimes one order may not be optimal.
    permutations_list = permutations_list[0]
    for i in range(len(permutations_list)/2):
        p1 = permutations_list[2*i]
        p2 = permutations_list[2*i+1]
#        print p1
#        print p2
        min_dists = str(min(greedy_breakpoint_bfs(p1, p2), greedy_breakpoint_bfs(p2, p1)))
        print min_dists, 

#    # Print and save the answer.
#    print ' '.join(min_dists)
#    with open('REAR.txt', 'w') as output_data:
#        output_data.write(' '.join(min_dists))
        
        
        
###meet in the middle way On step 2k we generate the set all the permutations which are on reverse distance equal to k from the first permutation; on step 2k+1 we generate the set all the permutations which are on reverse distance equal to k from the second permutation. After each step we check whether the two sets intersect (which means that we found where two shortest paths meet for the first time => form a global shortest path).

#def best_intersection(P, Q):
#  for perm in P:
#    if perm in Q:
#      return P[perm] + Q[perm]
#  return -1
#
#def make_step(processed, border, next_border):
#  for perm in border:
#    for j in range(len(perm)+1):
#      for i in range(j-1): # at least 2 numbers reversed
#        new_perm = perm[:i] + perm[i:j][::-1] + perm[j:]  # reverse [i,j]
#
#        if new_perm not in processed and new_perm not in border:
#          next_border[new_perm] = border[perm] + 1
#
#  processed.update(border)
#  border.clear()
#  border.update(next_border)
#  next_border.clear()
#
#def rev_dist(perm1, perm2):
#  processed1 = {}
#  border1 = {}
#  next_border1 = {}
#
#  processed2 = {}
#  border2 = {}
#  next_border2 = {}
#
#  border1[tuple(perm1)] = 0
#  border2[tuple(perm2)] = 0
#
#  lamp = False
#  while best_intersection(border1, border2) == -1:
#    if lamp:
#      make_step(processed1, border1, next_border1)
#    else:
#      make_step(processed2, border2, next_border2)
#    lamp = not lamp
#
#  return best_intersection(border1, border2)