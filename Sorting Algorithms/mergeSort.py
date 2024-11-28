def merge_sort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    mid = n//2
    
    l_half = arr[:mid]
    r_half = arr[mid:]
    
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    
    return merge(l_half, r_half)

def merge(left, right):
    new = []
    
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
            
    new.extend(left[i:])
    new.extend(right[j:])
    
    return new

arr = [64, 34, 25, 12, 22, 11, 90, 5]

print(merge_sort(arr))