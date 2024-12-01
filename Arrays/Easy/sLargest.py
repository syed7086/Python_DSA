def largest(arr):
    largest = arr[0]
    
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    
    return second_largest(arr, largest)

def second_largest(arr, largest):
    sLargest = -1
    
    for i in range(len(arr)):
        if arr[i] > sLargest and arr[i] != largest:
            sLargest = arr[i]
            
    return sLargest

arr = [3, 2, 1, 5, 7]

print(largest(arr))