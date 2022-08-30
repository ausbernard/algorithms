def divisible(n):
    dn = 0
    nums = [i for i in range(1,n+1)]
    result = [num for num in nums if n % num == 0 and num < n]
    for n in result: dn += n
    return dn


def amicable_num(n):
    result = []
    for x in range(1, n + 1):
        y = divisible(x)
        if divisible(y) == x and x != y:
            result.append(int(x+y))
    return result

sum_final = 0
answer = amicable_num(10000)
res = sorted([*set(answer)])
for i in res:
    sum_final += i
print(sum_final)


