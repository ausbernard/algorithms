def power_digit_sum(n):
    result = 0
    list_summ = [i for i in str(2**n)]
    for i in list_summ:
        result += int(i)
        
    return result
    
print(power_digit_sum(1000))