class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        map = dict.fromkeys(nums, 1)

        max_count = 1
        current_count = 1

        for num in nums:
            if num - 1 not in map.keys(): # this is a possible start value
                start = num
                while (start + 1 in map.keys()):
                    current_count += 1
                    start += 1
                
                if (current_count > max_count): max_count = current_count

                current_count = 1

        return max_count
