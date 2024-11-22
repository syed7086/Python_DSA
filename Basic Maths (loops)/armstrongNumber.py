def armstrongNumber(n):
    sum = 0
    dup = n
    while n > 0:
        lastDigit = n % 10
        sum = sum + lastDigit ** 3
        n //= 10
        
    return sum == dup

print(armstrongNumber(123))