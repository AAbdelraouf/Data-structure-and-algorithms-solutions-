# Solution from the EPI book #

def compute_random_permutation(n):
    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation
## random_sampling mentioned above isn't defined anywhere ##
compute_random_permutation(10)


# My solution with help of permutations library #
from itertools import permutations 
  
# # Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3]) 
  
# Print the obtained permutations 
for i in list(perm):
    print(i)
