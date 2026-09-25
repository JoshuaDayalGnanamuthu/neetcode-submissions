class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for index, value in enumerate(nums):
            complement = target - value
            if complement in map:
                return [map[complement], index]
            else:
                map[value] = index