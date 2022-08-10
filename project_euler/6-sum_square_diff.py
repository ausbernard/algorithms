"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time

def sum_of_squares(n):
    sum_squares = 0
    for i in range(1, n + 1):
        square = (i**2)
        sum_squares += square
    return sum_squares

def square_of_sums(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    squared_sum = (sum**2)
    
    return squared_sum

def euler_of_squares(limit):
    sum = limit*(limit + 1)/2
    sum_sq = ((2*limit) + 1)*(limit + 1)*limit/6
    
    return int((sum**2) - sum_sq)

if __name__ == "__main__":
    tic = time.perf_counter()     
    euler_of_squares(10)
    toc = time.perf_counter()
    print(f"Eueler algo took: {toc - tic:0.9f} seconds")
    tic = time.perf_counter()     
    sum_squares = sum_of_squares(10)
    sqaured_sum = square_of_sums(10)
    toc = time.perf_counter()
    print(f"My algo took: {toc - tic:0.9f} seconds")

    print(sqaured_sum - sum_squares)