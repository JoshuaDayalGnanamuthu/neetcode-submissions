class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        d1 = Counter(s)
        d2 = Counter(t)
        return d1==d2
        