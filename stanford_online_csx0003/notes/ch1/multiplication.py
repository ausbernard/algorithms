x = 5678
y = 1234
n = 8

def integer_multiplication(x, y, n):
  """As we think of n-digits getting larger the number of operations grows by n^2.

  Args:
      x (int): n-digit numbers
      y (int): n-digit numbers

  Returns:
      int: product of x*y
  
    5678
  x 1234
  ______
    22712
  17034-
  11356--
  5678---
  _______
  7006652
  """
  prim_operations = ((2*n)**2)
  
  return x * y, int(prim_operations)

def karatsuba_multiplication(x,y):
  """As we think of n-digits getting larger the number of operations grows by n^2.

  Args:
    x (int): n-digit numbers
    y (int): n-digit numbers

  Returns:
    int: product of x*y
  """
  x_str = str(x)
  y_str = str(y)
  
  a = int(x_str[0:2])
  b = int(x_str[2:4])
  c = int(y_str[0:2])
  d = int(y_str[2:4])
  
  step_two = a*c
  step_two_str = str(step_two)
  step_three = b*d
  step_four = (a+b)*(c+d)
  step_five = step_four - step_three - step_two
  step_five_str = str(step_five)
  answer = (int(step_two_str.ljust(4 + len(step_two_str), '0'))) + step_three + int(step_five_str.ljust(2 + len(step_five_str), '0'))
  
  return answer

def recursive_multipliation(m,n):
  # if either value are less than 10 multiply, else recurse into smaller numbers
  if m< 10 or n <10:
    return m * n
  else:
    mstring = str(m)
    nstring = str(n)
    # calculate the size of the numbers
    m = max(len(mstring), len(nstring))
    mid = int(m / 2)
    # split the numbers in the middle
    a = int(mstring[:-mid])
    c = int(nstring[:-mid])
    b = int(mstring[-mid:])
    d = int(nstring[-mid:])
    
    ac = recursive_multipliation(a,c)
    bd = recursive_multipliation(b,d)
    ad_plus_bc = recursive_multipliation(a+b,c+d) - ac -bd
    prod = ac * 10**(2*mid) + ad_plus_bc*10**(mid) + bd
    
    return prod


ans1, prim_op1 = integer_multiplication(x,y,n) 
ans2 = karatsuba_multiplication(x,y)

print(ans1)
print(ans2)
