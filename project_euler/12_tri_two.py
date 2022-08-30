import itertools

def div(n):
    d = 0
    for i in range(1, int(n**.5) +1):
        if (n % i) == 0:
            d += 1
    
    return 2*d

s = 0
for i in itertools.count(1):
    #rolling sum
    s += i
    if div(s) > 500:
        print(s)
        break
    