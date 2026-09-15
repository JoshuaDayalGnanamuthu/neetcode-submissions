class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        map = dict.fromkeys(nums, 1)

        start_indices = set()

        for i in map.keys():
            if (not map.get(i - 1)):
                start_indices.add(i)
        
        max_count = 1
        current_count = 1

        for i in start_indices:
            next = i +1
            while (next in map.keys()):
                current_count += 1
                next +=1
            if (current_count > max_count):
                max_count = current_count
            
            current_count = 1
        
        return max_count
