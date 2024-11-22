def stringPalindrome(Str):
    n = len(Str)
    
    left = 0
    right = n - 1
    
    while left < right:
        if not Str[left].isalnum():
            left += 1
        elif not Str[right].isalnum():
            right -= 1
        elif Str[left].lower() != Str[right].lower():
            return False
        else:
            left+=1
            right-=1
    return True


