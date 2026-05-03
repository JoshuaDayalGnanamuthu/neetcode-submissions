class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        max_area = 0

        while high > low:
            current_area = (high - low) * min(heights[high], heights[low])
            if current_area > max_area:
                max_area = current_area
            
            if heights[high] >= heights[low]:
                low += 1
            
            elif heights[low] > heights[high]:
                high -= 1
        
        return max_area
        