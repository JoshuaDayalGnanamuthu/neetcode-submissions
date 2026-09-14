class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        count = Counter(nums)
        result = [[] for _ in range(len(nums))]

        for key, value in count.items():
            result[value - 1].append(key)
        
        op = []
        for i in range(len(result) - 1, -1, -1):
            for num in result[i]:
                op.append(num)
                if len(op) == k:
                    return op
        
        return op

        