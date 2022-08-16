

seq = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
seq_str = str(seq)
seq_list = []
for i in seq_str:
    seq_list.append(i)
# seq_list = [2,4,6,8,10,12,14,16,18]
item = len(seq_list) 
end = len(seq_list) - 1


def multiply_digits(digits):
    a = int(digits[0])
    b = int(digits[1])
    c = int(digits[2])
    d = int(digits[3])
    e = int(digits[4])
    f = int(digits[5])
    g = int(digits[6])
    h = int(digits[7])
    i = int(digits[8])
    j = int(digits[9])
    k = int(digits[10])
    l = int(digits[11])
    m = int(digits[12])
    dig = f"{a} * {b} * {c} * {d} * {e} * {f} * {g} * {h} * {i} * {j} * {k} * {l} * {m}"
    multiplied = a*b*c*d
    
    return multiplied, dig

def backward(seq_list, idx, n):
    """
    find backwards options
    returns: Boolean (True or False)
    """
    if idx < n - 1:
        return False
    else:
    # if idx >= n:
        return True

def forward(seq_list, idx, n):
    """
    find Forward options
    returns: Boolean (True or False)
    """
    if idx == 0:
        return True
    if idx > (end-(n-1)):
        return False
    else:
        return True


def main(seq_list, n):
    start = 0
    end = n
    largest_total = 0
    sequence = []
    for i in seq_list:
        idx = seq_list.index(i)
        if not backward(seq_list, idx, n):
            # cannot go backwards
            pass
        else:
            try:
                start = start + 4
                end = end + 4
                # backward_end = n - (n - 1)
                # four_digits = (seq_list[i:-backward_end])
                # print(four_digits)
                # total, dig = multiply_digits(four_digits)
                # if total > largest_total:
                #     largest_total = total
                #     sequence = dig
                #     start += n
                #     end += n
                
            except IndexError:
                print("caught it")
        if not forward(seq_list, idx, n):
            # you cannot go forward
            start = start + 4
            end = end + 4
        else:
            try:
                # you can go forward
                four_digits = (seq_list[start:end])
                print(four_digits)
                total, dig = multiply_digits(four_digits)
                if total > largest_total:
                    largest_total = total
                    sequence = dig
                    start += n
                    end += n
            except IndexError:
                break
    
    print(f"largest sequence: {sequence} = {largest_total}")

main(seq_list, n=13)


    # length = len(seq_list)
    # if length <= num
    #     values_before = []
    #     values_after = []
    #     value_to_check = seq_str[i]



    # start = 0
    # end = 4
    # sequence = ""
    # largest_total = 0
    # for i in range(int(len(seq_str)/end)):
    #     four_digits = (seq_str[start:end])
    #     total, dig = multiply_digits(four_digits)
    #     if total > largest_total:
    #         largest_total = total
    #         sequence = dig
    #     start += 4
    #     end += 4
    # print(f"{sequence} = {largest_total}")
