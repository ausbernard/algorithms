def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sum = 0
temp_fact = [ i for i in str(factorial(100))]
for i in temp_fact:
    sum += int(i)

print(sum)