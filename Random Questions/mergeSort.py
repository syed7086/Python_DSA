def mergeSort( arr, l, r):
    if l < r:
        # Step 1: Find the middle point
        m = (l + r) // 2

        # Step 2: Recursively sort the two halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # Step 3: Merge the sorted halves
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    # Sizes of two subarrays
    n1 = m - l + 1
    n2 = r - m

    # Temporary arrays
    L = arr[l:m + 1]  # Left subarray
    R = arr[m + 1:r + 1]  # Right subarray

    # Merge the temporary arrays back into arr[l..r]
    i = j = 0
    k = l # Tracking in orginal array

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        

arr = [38, 27, 43, 3, 9, 82, 10]
n = len(arr)

mergeSort(arr, 0, n - 1)
print("Sorted array is:", arr)