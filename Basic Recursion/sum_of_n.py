sum = 0

def func(i,n):
    global sum
    
    if i>n:
        return
    sum+=i
    func(i+1, n)
    
# n = int(input('Enter something: '))
# func(1,n)
# print(f'The sum of first {n} consecutive numbers is {sum}')

def fun(i, sum):
    if i < 1:
        print(sum)
        return
    fun(i-1, sum + i)

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(3))