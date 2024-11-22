def primeCheck(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if(n%i == 0):
            count += 1
            if (int(n/i) != i):
                count += 1  
    if (count == 2):
        print('Prime')
    else:
        print('Not Prime')


primeCheck(2)


def prime(n):
    count = 0
    for i in range(1 , n+1):
        if n%i == 0:
            count+=1
    
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")
        
prime(6)