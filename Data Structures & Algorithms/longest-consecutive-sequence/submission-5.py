class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        from collections import Counter
        count = Counter(nums)
        keys = sorted(count.keys())

        max_stream = 0
        current_stream = 1

        print(keys)

        for i in range(len(keys) - 1):
            if (keys[i + 1] - keys[i]) == 1:
                current_stream += 1
            else:
                if (current_stream >= max_stream):
                    max_stream = current_stream
                current_stream = 1
        else:
            if (current_stream >= max_stream):
                    max_stream = current_stream

        return max_stream


        