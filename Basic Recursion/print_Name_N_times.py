def func(i,n):
    if i>n:
        return
    print("Syed")
    func(i+1, n)

n = int(input('Enter some number:'))
func(1,n)

