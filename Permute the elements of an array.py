# Solution from the EPI book  #
# from test_framework import generic_test

def apply_permutation(perm, A):

    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp
    # Restore perm.
    perm[:] = [a + len(perm) for a in perm]

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A



# A Python program to print all  
# permutations using library function 
from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3]) 
  
# Print the obtained permutations 
for i in list(perm):
    print(i)