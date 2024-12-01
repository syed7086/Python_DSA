def checkSorted(arr):
    for i in range(len(arr)):
        if arr[i] >= arr[i-1]:
            return False
    return True
    
arr = [3,4,5,1,2]

print(checkSorted(arr))