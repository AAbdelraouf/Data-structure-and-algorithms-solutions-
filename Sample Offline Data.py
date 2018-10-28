import random
randomNumbers = random.randint(1,10)
print(randomNumbers)



def random_sampling(k, A):

    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

# Pythonic solution
def random_sampling_pythonic(k, A):
    A[:] = random.sample(A, k)