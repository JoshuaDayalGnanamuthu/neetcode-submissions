class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalnum():
                word += i.casefold()
        
        low = 0
        high = len(word) - 1 

        while (high > low):
            if (word[low] != word[high]): return False
            high -= 1
            low += 1
        
        return True

        