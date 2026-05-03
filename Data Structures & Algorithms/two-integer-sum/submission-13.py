class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = dict()

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index_list.keys():
                return [index_list[difference], i]
            index_list[nums[i]] = i
        
        



        