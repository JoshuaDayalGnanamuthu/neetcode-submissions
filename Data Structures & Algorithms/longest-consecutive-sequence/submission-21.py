class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_sequence = 0

        for num in nums:
            if num - 1 not in seen:
                current_sequence = 1
                while num + 1 in seen:
                    current_sequence += 1
                    num = num + 1
                max_sequence = max(max_sequence, current_sequence)
            
        return max_sequence
