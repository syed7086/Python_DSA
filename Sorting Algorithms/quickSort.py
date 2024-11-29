def quickSort(arr, low, high):
    if low<high:
        pIndex = partition(arr, low, high)
        
        quickSort(arr, low, pIndex-1)
        quickSort(arr, pIndex+1, high)
    return arr
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    
    return j
    
arr = [64, 34, 25, 12, 22, 11, 90, 5]

quickSort(arr, 0, len(arr)-1)

print(quickSort(arr, 0, len(arr)-1))
