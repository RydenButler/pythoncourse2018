## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(a, b):
    bigger = max(a,b)
    smaller = min(a,b)
    if smaller == 0:
        return bigger
    else:
        remainder = bigger%smaller
        return gcd(smaller, remainder)


## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
    if me == 0:
        return primes
    else:
        is_prime = 1
        for i in range(1, me):
            is_prime = max(is_prime, gcd(me, i))
        if is_prime == 1:
            primes.insert(0, me)              
        return find_primes(me-1, primes)

