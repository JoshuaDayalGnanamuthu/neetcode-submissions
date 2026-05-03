class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 1):
            low = i + 1
            high = len(nums) - 1
            target = -nums[i]

            while high > low:
                if nums[high] + nums[low] == target:
                    if ([nums[i], nums[low], nums[high]] not in result):
                        result.append([nums[i], nums[low], nums[high]])
                    low += 1
                if nums[high] + nums[low] > target:
                    high -= 1
                if nums[high] + nums[low] < target:
                    low += 1
                
        return result

        