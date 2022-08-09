"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# general principle and how to solve it
    # use a recursion approach
    # Rho Algorithm - prime factorization (large numbers)

# Problem
# ..
# .
# Find the prime numbers within (1 to range(<int>))
    # Is the number in position only divisible by 1 and itself?
    # eq1 = ((6*n) + 1)
    # eq2 = ((6*n) - 1)
    # because we don't want numbers beyond our 'natural_number' exclude all primes that are above the number we intended to get.
def prime_numbers(natural_num):
    primes = [2,3]
    for n in range(1, natural_num):
        x, y = 6 * n + 1, 6 * n - 1
        if x <= natural_num:
            primes.append(x)
        if y <= natural_num:
            primes.append(y)

    return primes


# from out list of primes (prime_numbers(int)), we find out which ones multiplied together give us our total - prime factor.
    # Keep mulitplying your primes until you get the total.

def prime_factors(natural_num):
    primes = prime_numbers(natural_num)
    # test all integers less than square root of natural_num (n^(1/2))
    num_square_root = int(natural_num**(1/2))
    rho_primes = [i for i in primes if i < num_square_root]

    


prime_factors(315)