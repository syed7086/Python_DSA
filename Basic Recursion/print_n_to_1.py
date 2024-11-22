# Parametrized Way
def func(i, n):
    if i>n:
        return
    print(n)
    func(i, n-1)

# Functional Way
def printNos(n):
    if n==0:
        return
    print(n, end=' ')
    printNos(n-1)


n = int(input('Enter something: '))

printNos(n)