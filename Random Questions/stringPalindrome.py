def palindrome(a):
    n = len(a)
    
    left = 0
    right = n - 1
    
    while left < right:
        if not a[left].isalnum():
            left += 1
        elif not a[right].isalnum():
            right -= 1
        elif a[left] != a[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

Str1 = 'This is not a Palindrome'
Str2 = 'abcddcba'
print(palindrome(Str2))  
    