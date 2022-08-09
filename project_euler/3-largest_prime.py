"""Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import random

def prime_numbers(natural_num):
    primes = [2,3]
    for n in range(1, natural_num):
        x, y = 6 * n + 1, 6 * n - 1
        if x <= natural_num:
            primes.append(x)
        if y <= natural_num:
            primes.append(y)

    return primes


def prime_factors(natural_num):
    primes = prime_numbers(natural_num)
    # test all integers less than square root of natural_num (n^(1/2))
    num_square_root = int(natural_num**(1/2))
    rho_primes = [i for i in primes if i < num_square_root]
    # initialize i to 1
    i = 1
    # initialize x to a random int in our list
    x = random.choice(rho_primes)
    # save the value of x 
    y = x
    # 
    k = 2
    # while loop 
    while True:
        # increment i
        i = i + 1
        

    


prime_factors(315)

"""Story
    # general principle and how to solve it
        # use a recursion approach
        # Rho Algorithm - prime factorization (large numbers)
    # Problem
        # Find the prime numbers within (1 to range(<int>))
        # Is the number in position only divisible by 1 and itself?
        # eq1 = ((6*n) + 1)
        # eq2 = ((6*n) - 1)
        # Cause we don't want numbers beyond our 'natural_number' exclude all primes that are above the number we intended to get.
        # from out list of primes (prime_numbers(int)), we want to decompose into a product of primes.
        # Cause the natural_number is large we will give Rho Algo a try. Positives, are it works well with large numbers and always returns primes - if it returns. The downside is it may not work and return anything sometimes. It's not a garunteed algorithm.
            # test all integers less than square root of natural_num (n^(1/2))
            # initialize i to 1
            # initialize x to a random int in our list


"""