class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        count1 = Counter(s)
        count2 = Counter(t)
        return count1 == count2


        
        