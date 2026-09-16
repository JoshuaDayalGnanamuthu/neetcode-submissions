class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        results = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                target = nums[i] + nums[left] + nums[right]

                if (target == 0): 
                    results.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                
                elif (target < 0):
                    left += 1
                
                else:
                    right -= 1

        return [list(value) for value in results]
                
        