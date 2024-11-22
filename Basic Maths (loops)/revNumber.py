def revNumber(n):
    revN = 0
    while n > 0:
        lastDigit = n % 10
        revN = (revN * 10) + lastDigit
        n //= 10
        
    return revN

print(revNumber(234))