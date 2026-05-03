class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        d1 = Counter(nums)
        if not d1:
            return False
        if max(d1.values())>1:
            return True
        return False