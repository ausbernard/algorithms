def factorial(n):
    if  n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def lattice(n):
    """
    Binomial_coefficient 
    """
    numerator = factorial((2*n))
    denominator = factorial(n) ** 2
    result = numerator // denominator
    
    return result

print(lattice(5))