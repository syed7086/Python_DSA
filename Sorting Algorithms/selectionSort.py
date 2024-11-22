def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_idx = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr


def select(arr, i):
    min_idx = i
    
    for j in range(i+1, len(arr)):
        if arr[j]<arr[min_idx]:
            min_idx = j
            
    return min_idx

def selection(arr,n):
    for i in range(n-1):
        min = select(arr,i)
        
        arr[i], arr[min] = arr[min], arr[i]
    return arr
        
    
        
    
arr=[2,12,4,54,6,1]

print(selection(arr,))
        