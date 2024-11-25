def insertionSort(arr):
    n = len(arr)
    
    for i in range(1, n):
        insert_index = i
        current_value = arr.pop(i)
        
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        
        arr.insert(insert_index, current_value)
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90, 5]

print(insertionSort(arr))        

