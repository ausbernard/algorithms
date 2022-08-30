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
