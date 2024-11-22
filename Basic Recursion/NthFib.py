def nThFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return nThFib(n-1) + nThFib(n-2)

print(nThFib(3)) 