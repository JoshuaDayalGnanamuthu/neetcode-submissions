class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while high > low:
            if not s[low].isalnum():
                low += 1
                continue
            
            if not s[high].isalnum():
                high -= 1
                continue
            
            if s[high].lower() != s[low].lower():
                return False
            
            low += 1
            high -=1
        
        return True
        