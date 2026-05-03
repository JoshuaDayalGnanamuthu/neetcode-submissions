class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        for index,i in enumerate(nums):
            if (j := target-i) in nums[index+1:]:
                return [nums.index(i),nums[index+1:].index(j)+index+1]