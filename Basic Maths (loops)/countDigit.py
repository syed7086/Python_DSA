def countDigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
        
    print(count)

def revNumber(n):
    revN = 0
    while n > 0:
        lastDigit = n % 10
        n = n // 10
        revN = (revN * 10) + lastDigit
        
    print(revN)
    
def palindrome(n):
    rev_n = 0
    original = n

    while n > 0:
        rev_n = rev_n * 10 + n % 10
        n //= 10

    return rev_n == original



def reverse(x: int) -> int:
    rev_n = 0
    # sign = -1 if x < 0 else 1
    # x = abs(x)

    while x > 0:
        last_digit = x % 10
        x //= 10
        rev_n = rev_n * 10 + last_digit

    # rev_n *= sign

    return rev_n


def armStrong(n):
    sum = 0
    check = n
    while n > 0:
        lastDigit = n % 10
        sum = sum + (lastDigit ** 3)
        n //= 10
        
    return sum == check


def divisors(n):
    for i in range (1, n + 1):
        if(n%i == 0):
            print(i, end=' ')
            
    
# optimised approach
from math import sqrt
def divisor(n):
    num = int(sqrt(n))
    for i in range(1, num + 1):
        if(n%i == 0):
            print(i, end=' ')
            
        if(n/i != i):
            print(i)


divisors(36)
