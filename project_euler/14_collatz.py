import itertools

def odd(n):
    return (3*n) + 1

def even(n):
    return n//2

def chain(n):
    chain = [n]
    while chain[-1] != 1:
        if n % 2 == 0:
            n = even(n)
            chain.append(n)
        else:
            n = odd(n)
            chain.append(n)
    
    return len(chain)

s = 0
for i in itertools.count(1):
    if i < 1000000:
        r = chain(i)
        if r > s:
            s = r
            print(f"{i} with len: {s}")
    else:
        break
    
# 837799 with len: 525