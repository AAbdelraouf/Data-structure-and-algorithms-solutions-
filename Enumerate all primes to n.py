
def list_of_primes(n):
    primes = []
    for y in range (2, n):
        for z in range(2, y):
            if y % z == 0:
                break
        else:
            primes.append(y)
            primes.sort()
    return primes

print(list_of_primes(100))