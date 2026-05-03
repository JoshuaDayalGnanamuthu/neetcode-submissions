class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        values = [0] * 26
        print(values)
        for i in range(len(s)):
            values[ord(s[i]) - 97] += 1
            values[ord(t[i]) - 97] -= 1
        
        for i in values:
            if i: return False

        return True
        
        