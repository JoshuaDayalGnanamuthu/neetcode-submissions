class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums))]

        for key, value in counter.items():
            buckets[value - 1].append(key)
        results = []

        while k:
            if buckets[-1] != []:
                results.append(buckets[-1].pop())
                k -= 1
            else:
                buckets.pop()
        
        return results

                

        