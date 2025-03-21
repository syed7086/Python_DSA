def palindrome(s):
    n = len(s)
    
    left = 0
    right = n - 1
    
    while left < right:
        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True




# Leetcode Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True


Str = 'AbcDCBA'

print(palindrome(Str))