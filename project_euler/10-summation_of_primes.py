"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numbers
import time

def is_prime(n):
    # 1 cannot be prime
    if n == 1:
        return False
    else:
        # if 2 or 3 return prime
        if n < 4:
            return True
        else:
            # if even return False
            if n % 2 == 0:
                return False
            else:
                # if below 9 return false, cus we took out 4,6,8
                if n < 9:
                    return True
                else:
                    # if divisble by 3 return False
                    if n % 3 == 0:
                        return False
                    else:
                        r = int(n**(1/2))
                        f = 5
                        while f <= r:
                            # if divisible by 5 return False
                            if n % f == 0:
                                return False
                            # if divisible by 7 return False
                            if n % (f+2) == 0:
                                return False
                            f += 6
    return True

def sum_primes(primes):
    sum = 0
    for i in primes:
        if isinstance(i, numbers.Number):
            sum += i
            
    return sum
    
if __name__ == "__main__":
    tic = time.perf_counter()
    primes = [2]
    count = 1
    limit = 2000000
    num = 1

    while count <= limit:
        # take only odds
        if is_prime(num):
            if num <= limit:
                primes.append(num)
        num += 2
        count += 1

    print(sum_primes(primes))
    toc = time.perf_counter()
    
    print(f"the time elapsed: {toc - tic}")


                        
    
    
