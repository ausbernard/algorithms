"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time


def is_palindome(num):
    reversed = int(str(num)[::-1])
    if num == reversed:
        return True
    else:
        return False

def generate_num():
    tic = time.perf_counter()
    largest_palindrome = 0
    for first_num in range(100,1000):
        for second_num in range(100,1000):
            product = first_num * second_num
            if is_palindome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
    
    toc = time.perf_counter()
    print(f"Your fibonacci algo took: {toc - tic:0.9f} seconds")
    
    return largest_palindrome


if __name__=='__main__':
    print(generate_num())