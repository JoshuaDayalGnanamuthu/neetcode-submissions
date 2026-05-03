class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x, y in enumerate(nums):
            if target - y in nums[x+1:]:
                return [x, x + 1 + nums[x+1:].index(target - y)]

        