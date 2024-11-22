def palindrome(n):
    revN = 0
    dup = n
    while n > 0:
        revN = (revN * 10) + (n % 10)
        n //= 10
        
    return revN == dup

print(palindrome(121))