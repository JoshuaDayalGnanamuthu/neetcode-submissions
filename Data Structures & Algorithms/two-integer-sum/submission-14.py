class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = dict()

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index.keys():
                return [index[difference], i]
            index[nums[i]] = i
        
        



        