"""Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
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
    prime_facts = []
    # print the number of two's that divide n
    while natural_num % 2 == 0:
        natural_num = natural_num / 2
    
    # assuming n is odd at this point, skip 2 to get the odds
    for i in range(3, int(math.sqrt(natural_num))+1, 2):
        # i divide n, print i and divide n
        while natural_num % i == 0:
            # print(i),
            natural_num = natural_num / i
            prime_facts.append(i)


    return prime_facts

def sort_prime_factors(natural_num):
    prime_factorials = prime_factors(natural_num)
    index_length = len(prime_factorials) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if prime_factorials[i] > prime_factorials[i+1]:
                sorted = False
                prime_factorials[i], prime_factorials[i+1] = prime_factorials[i+1], prime_factorials[i]
    
    return prime_factorials[-1]
    
                
print(sort_prime_factors(600851475143))

"""Story - Return to RHO
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
        # Cause the natural_number is large we will give Rho Algo a try. Positives, are it works well with large numbers and always returns primes - if it returns. The downside is it may not work and return anything sometimes. It's not a garunteed algorithm. (time complexity: θn^(1/2))
            # test all integers less than square root of natural_num (n^(1/2))
            # initialize i to 1
            # initialize x to a random int in our list

def modular_power(base, exponent, modulus):
    i = 1

    while (exponent > 0):
        #if y is odd, multiply base with result
        if (exponent & 1 ):
            i = (i * base) % modulus
        # exponent = exponent/2
        exponent = exponent >> 1
        
        # base = base * base
        base = (base * base) % modulus
    
    return i

def prime_factors(natural_num):
    primes = prime_numbers(natural_num)
    # test all integers less than square root of natural_num (n^(1/2))
    num_square_root = int(natural_num**(1/2))
    rho_primes = [i for i in primes if i < num_square_root]
    # disregard 1 - no prime divisor
    if (natural_num == 1):
        return 1
    # even means one of the divisors is 2
    if natural_num % 2 == 0:
        return 2
    # initialize x to a random int in our list
    x = (random.randint(0,2) % (natural_num - 2))
    # save the value of x 
    y = x
    # constant in f(x)
    # if c throws an error it will choose a different c, especially if c is a composite
    c = random.randint(0,1) % (natural_num - 1)
    # initialize k for the divisor (result)
    k = 1
    # while loop to continue until prime factor isn't found
    while (k == 1):
        
        # Tortoise Move: x(i+1) = f(x(i))
        x = (modular_power(x, 2, natural_num) + c + natural_num) % natural_num
        # Hard Move: y(i+1) = f(f(y(i)))
        y = (modular_power(x, 2, natural_num) + c + natural_num) % natural_num
        y = (modular_power(x, 2, natural_num) + c + natural_num) % natural_num
        # check gcd of |x-y| and n
        k = math.gcd(abs(x-y), natural_num)
        
        #retry if algo fails to find the prime factor
        if (k == natural_num):
            return prime_factors(natural_num)

    return k
"""