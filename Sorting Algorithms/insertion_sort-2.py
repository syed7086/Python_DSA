# Insertion Sort without using pop and insert

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
        
arr = [64, 34, 25, 12, 22, 11, 90, 5]
insertion_sort(arr)
print("Sorted array:", arr)