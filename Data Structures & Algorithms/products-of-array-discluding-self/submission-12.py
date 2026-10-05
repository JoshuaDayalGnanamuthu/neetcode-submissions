class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = nums[0]
        results = [1] * len(nums)

        for i in range(1, len(nums)):
            results[i] *= prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            results[i] *= suffix_prod
            suffix_prod *= nums[i]
        
        return results
        