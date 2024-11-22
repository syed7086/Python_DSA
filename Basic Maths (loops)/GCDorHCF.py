# def GCDorHCF(n1, n2):
#     GCD = 1
#     for i in range(1, min(n1, n2) + 1):
#         if (n1%i == 0 and n2%i == 0):
#             GCD = i
            
#     return GCD



# def GCDorHCF(n1, n2):
#     for i in range(min(n1,n2), 0, -1):
#         if(n1%i == 0 and n2%i == 0):
#             GCD = i
#             break
#     print(GCD)
    
def GCD ( n1, n2 ):
    while( n1 > 0 and n2 > 0 ):
        if( n1 > n2 ):
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    
    if ( n1 == 0 ):
        print(n2)
    else:
        print(n1)
        
            


