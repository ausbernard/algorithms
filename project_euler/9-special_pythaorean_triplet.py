
def is_pythagorean(a, b, c):
    if a < b < c:
        if a**2 + b**2 == c**2:
            return True
    
    return False


def mine():
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if is_pythagorean(a,b,c):
                    if a + b + c == 1000:
                        print(f"found triplet: a:{a}, b:{b}, c:{c}")
                        print(f"product = {a*b*c}")
                        break
                else:
                    pass

def euler():
    s = 1000
    for a in range(3,int((s-3)/3)):
        for b in range((a+1),int((s-1-a)/2)):
            c = s-a-b
            if c*c == a*a + b*b:
                print(f"found triplet: a:{a}, b:{b}, c:{c}")
                break

euler()
mine()

#mines is a lot less efficient but it works
    
