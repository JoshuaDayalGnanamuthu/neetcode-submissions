class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        counter = Counter(nums)
        heap = [(-value, key) for key, value in counter.items()]

        heapq.heapify(heap)
        results = []

        while k:
            results.append(heapq.heappop(heap)[1])
            k -= 1
        
        return results
        

                

        