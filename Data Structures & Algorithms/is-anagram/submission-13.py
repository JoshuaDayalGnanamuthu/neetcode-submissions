class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        frequency = [0] * 26

        for i in range(len(s)):
            frequency[ord(s[i]) - 97] += 1
            frequency[ord(t[i]) - 97] -= 1
        
        for i in frequency:
            if i: return False
        
        return True

        
        