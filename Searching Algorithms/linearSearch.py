def linearSearch (arr, n, k):
    for i in range(0, n):
        if (arr[i] == k):
            return i
    return -1
    
arr = [2, 3, 4, 6]

n = len(arr)

k = 2

result = linearSearch(arr, n, k)

if (result == -1):
    print('ELEMENT NOT FOUND')
else:
    print('ELEMENT FOUND at INDEX: ', result)