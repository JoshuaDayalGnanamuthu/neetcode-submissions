class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = nums[0]

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        sufix = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            result[i] *= sufix
            sufix *= nums[i]

        return result
        