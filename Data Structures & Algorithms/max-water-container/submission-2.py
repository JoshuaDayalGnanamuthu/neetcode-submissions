class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_volume = 0
        current_volume = 0

        while (left < right):
            height = right - left
            current_volume = height * min(heights[left], heights[right])

            if (current_volume > max_volume):
                max_volume = current_volume
            
            if (heights[left] >= heights[right]):
                right -= 1
            
            else:
                left += 1
        
        return max_volume