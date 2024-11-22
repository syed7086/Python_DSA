def select(arr, i):
    mini = i
    
    for j in range(i+1, len(arr)):
        if arr[j] < arr[mini]:
            mini = j
    return mini


def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        mini = select(arr,i)
        
        arr[i], arr[mini] = arr[mini], arr[i]
        
    return arr

arr = [13, 46, 32, 52, 9]

print(selectionSort(arr))