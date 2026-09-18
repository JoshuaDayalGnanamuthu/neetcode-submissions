class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for index, num in enumerate(nums):
            map[num] = index
        

        for index, num in enumerate(nums):
            value = target - num

            if (map.get(value, None) and map.get(value) != index ):
                return [min(map[value], index), max(map[value], index)]