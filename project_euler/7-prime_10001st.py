"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
from math import floor
import time

def to_infinity():
    index = 2
    while True:
        yield index
        index += 1

def is_prime(n):
    for i in range(2, 1+n//2):
        if n % i == 0:
            return False
    else:
        return True
    
def prime_location(n):
    primes = []
    for i in to_infinity():
        if is_prime(i):
            primes.append(i)
        if len(primes) == n:
            print(primes[-1])
            break
        
## Faster Algorithm ##

def sieve_de_austhenes(n):
    if n == 1:
        return False
    else:
        if n < 4:
            return True #// 2 and 3 are primes
        else:
            if n % 2 == 0:
                return False
            else:
                if n < 9:
                    return True #//we have already ruled out 4, 6, 8
                else:
                    if n % 3 == 0:
                        return False
                    else:
                        r = floor(n**(1/2))
                        print(r)
                        f = 5
                        while f <= r:
                            if n % f == 0:
                                return False
                            if n % (f+2) == 0:
                                return False
                            f = f + 6
    return True

def prime_nth(limit):
    count = 1  #//we know that 2 is a prime
    candidate = 1
    while count < limit:
        candidate += 2    #//only want the odd numbers (not divisible by 3, 5, 7) to pass through function
        if sieve_de_austhenes(candidate):
            count += 1
    print(candidate)

prime_nth(10001)
# test: sieve_de_austhenes(23)
        

# We ruled out recursion. Since n > 169 (n < 169 with a total of 1000 for the python interpreter limit for recursion functions) - needed a different approach: https://codefather.tech/blog/recursion-error-python/

# sieve of erathosthenes information: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


