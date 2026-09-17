class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False # cannot be an anagram if they dont have the same length
        
        chars = [0] * 26 # create a list that acts as an counter for each of the 26 aplhabets

        for i in range(len(s)):
            chars[ord(s[i]) - 97] += 1
            chars[ord(t[i]) - 97] -= 1 # update the counter for one, and decrement for the other
        
        for counter in chars:
            if counter != 0: return False
        
        return True

        