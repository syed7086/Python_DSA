def mergeSort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    m = n // 2
    
    L = arr[:m]
    R = arr[m:]
    
    L = mergeSort(L)
    R = mergeSort(R)
    
    return merge(L,R)

def merge(left, right):
    new = []
    
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
            
    new.extend(left[i:])
    new.extend(right[j:])
    
    return new


arr = [64, 34, 25, 12, 22, 11, 90, 5]

print(mergeSort(arr))