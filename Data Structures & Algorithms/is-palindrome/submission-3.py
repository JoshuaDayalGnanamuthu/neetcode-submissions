class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while (high > low):
            if (not (s[low].isalnum())):
                low += 1
                continue
            elif (not (s[high].isalnum())):
                high -= 1
                continue
            
            if (s[low].lower() != s[high].lower()): 
                print(s[low], s[high])
                return False
            
            low += 1
            high -= 1
        
        return True
        