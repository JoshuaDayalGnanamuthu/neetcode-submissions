class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for index, value in enumerate(nums):
            map[value] = index
        
        for i in range(len(nums)):
            if (target - nums[i] in map and map[target - nums[i]] != i):
                return [min(i, map[target - nums[i]]), max(i, map[target - nums[i]])]
