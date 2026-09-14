class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        chars = [0 for i in range(26)]

        for i in range(len(s)):
            chars[97 - ord(s[i])]+= 1
            chars[97 - ord(t[i])]-= 1
        
        for i in chars:
            if (i): return False;
        
        return True

        