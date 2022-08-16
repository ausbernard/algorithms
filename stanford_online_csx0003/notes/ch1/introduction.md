# Algorithms: Design and Analysis, Part 1

## Introduction
Can we do better? Is the mantra.

Talking about an algorithm (well designed set of rules) you would use the following pattern:
1. Define a computational problem
2. We will say what the input is
3. We will then say what the desired output is
4. Then we will proceed to give a solution (algorithm) that transforms the input to the output
5. We will assess the performance of this algorithm through number of basic operations that it performs

### The Grade-School Algorithm
#### Integer Multiplication
Upshot: As we think about (n) getting larger. The number of operations forour constant (4) grows by a factor of n^2 which is 16. 
Input: 2 n-digit numbers (x and y). Where n is large (> 1000)
Output: the product x * y
Algorithm: see integer_multiplication.py
Performance: Primitive opeprations (add or multiply 2 single-digit numbers). The number of basic operations to perform our first basic product (first number) is <=2n per row for n rows. 2n^2 + 2n^2 -> 2(4^2) + 2(4^2) -> 2(16) + 2(16) = 64.

#### Karatsuba Multiplication
Upshot: 
Input: 2 n-digit numbers (x and y)
Output: the product of 2 n-digit numbers (x and y)
Algorithm: It will be broken down into steps. Step one, is split the larger digit in half to be its own number for x and y. (ie: 5678 -> 56 & 78). 
    - x = 56 (a) & 78 (b)
    - y = 12 (d) & 34 (c)
Will do a sequence of operations involving only these double digit numbers. Then collect all terms together to get our desired output. Step 2 is to get the product of a x c. Step 3 is to get the product of b x d. Step 4 is to take the sum of a + b and multiply by the sum c + b. Step 5 is to subtract the first two products. Step 6 is take the product of step 2 and add 4 zeros (ie: 672 -> 6720000)
Performance = as n gets larger we run it 9(n)

#### Recursive Algorithm/Multiplication
Input: 2 n-digit numbers (x and y)
Output: the product of 2 n-digit numbers (x and y)
Algorithm: only three recursions which operate on smaller ints, are used to create the partial results
- recursively compute (a,c)
- recursively compute (b,d)
- recursively compute ()

