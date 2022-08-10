"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time


def to_infinity():
    index = 1
    while True:
        yield index
        index += 1

def slowest_multiple():
    found = False
    smallest_number = 0
    count = 0
    tic = time.perf_counter()
    while not found:
        for num in to_infinity():
            for divisor in range(1,21):
                if num % divisor == 0:
                    count += 1
                else:
                    count = 0
                    break
            if count == 20:
                smallest_number = num
                print(smallest_number)
                found = True
                break
    toc = time.perf_counter()
    print(f"Your algo took: {toc - tic:0.9f} seconds")

def fast():
    tic = time.perf_counter()
    i = 1
    for k in (range(1, 21)):
        print(f"top iteration {k}")
        if i % k > 0:
            print(f"if {i} / {k} > 0")
            for j in range(1, 21):
                print(f"next iteration {j}")
                if (i*j) % k == 0:
                    print(f"if {i} * {j} % {k} == 0")
                    i *= j
                    print(f"{i}*={j}")
                    print({f"i = {i}"})
                    break
    print(i)
    toc = time.perf_counter()
    print(f"Euler algo took: {toc - tic:0.9f} seconds")
    
if __name__ == "__main__":
    fast()
    slowest_multiple()

"""
lol first attempt:
232792560
Your algo took: 91.192764521 seconds
lawl

gonna make this faster:
"""