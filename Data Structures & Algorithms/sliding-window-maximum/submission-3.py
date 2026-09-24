class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        if len(nums) == 1:
            return nums
        
        heap = []
        results = []

        for index, value in enumerate(nums):
            heapq.heappush(heap, (-value, index))

            while (len(heap) and heap[0][1] <= index - k):
                heapq.heappop(heap)
            
            if (index >= k - 1):
               results.append(-heap[0][0])
        
        return results
                    



        