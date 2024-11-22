def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n+1):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = 4

print(fib(n))