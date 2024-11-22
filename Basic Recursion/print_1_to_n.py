# Parametrized way
def func(i, n):
    if i>n:
        return
    print(i)
    func(i+1,n)

# Parametrized way
def fun(i,n):
    if i>n:
        return
    fun(i+1,n)
    print(i)

# Functional way
def printNos(n):
    if n == 0:
        return
    printNos(n-1)
    print(n,end=' ')
    
printNos(3)
