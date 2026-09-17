class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # we use an hashmap beacus look up is O(1)

        for num in nums:
            if num in seen: return True
            else:
                seen.add(num)
        
        return False

        