def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

arr=[2,12,4,54,6,1]

print(bubbleSort(arr))