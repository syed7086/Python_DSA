# Iterative Approach
def revArr(arr, n):
    nArr = [0] * n
    for i in range(n-1, -1, -1):
        nArr[n-i-1] = Arr[i]
    
    print(nArr)

# Two-Pointer Approach
def reverseArr(arr, n):
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
        
    print(arr) 

    
        
    
Arr = [1 ,2, 3, 4, 5]
# n = len(Arr)
# rev(Arr, n)