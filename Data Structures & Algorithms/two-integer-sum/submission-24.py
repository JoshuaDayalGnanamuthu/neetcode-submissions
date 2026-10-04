class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = dict()

        for index, num in enumerate(nums):
            if target - num in index_map:
                return [index_map[target - num], index]
            index_map[num] = index
        
    