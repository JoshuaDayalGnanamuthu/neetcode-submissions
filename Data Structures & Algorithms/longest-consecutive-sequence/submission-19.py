class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen= set(nums)

        max_length = 1

        for num in nums:
            if (num - 1 not in seen):
                current_count = 1
                while (num + 1 in seen):
                    current_count += 1
                    num = num + 1
                if max_length < current_count:
                    max_length = current_count
        

        return max_length
