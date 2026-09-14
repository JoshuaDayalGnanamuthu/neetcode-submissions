class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for index, value in enumerate(nums):
            if (target - value) in map.keys():
                return [map[target - value], index]
            else:
                map[value] = index;
        
        return [-1, -1]
        