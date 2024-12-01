def second_largest_element(arr):
    if len(arr) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None

arr = [10, 20, 4, 45, 99]
print("Second largest element:", second_largest_element(arr))