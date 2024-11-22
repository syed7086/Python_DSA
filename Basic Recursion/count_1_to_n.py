cnt = 1

def print_count(n):
    global cnt # used when need to change the global variable
    
    if cnt == n:
        return
    
    print(cnt)
    cnt+=1
    
    print_count(n-1)
    
print_count(10)
