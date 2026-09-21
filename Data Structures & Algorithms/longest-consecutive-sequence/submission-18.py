class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_count = 1

        start_set = set()

        for num in nums: start_set.add(num)

        for num in nums:
            if (num -1 not in start_set):
                current_count = 1
                while (num + 1 in start_set):
                    current_count += 1
                    num += 1
            
                if current_count > max_count:
                    max_count = current_count
        
        return max_count    
