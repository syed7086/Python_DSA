# def divisors(n):
#     for i in range(1, n+1):
#         if(n%i == 0):
#             print(i, end=' ')
            

# divisors(36)


# More 
import math

def divisors(n):
    L = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if (n%i == 0):
            L.append(i)
            if((n/i) != i):
                L.append(n//i)
                
    L.sort()
    print(f'Divisors of {n} are: {L}')
                

divisors(36)
