class Solution:
    def trap(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        volume = 0

        while high > low:
            minimum_level = min(height[low], height[high])
            for i in range(low, high):
                if height[i] < minimum_level:
                    volume += minimum_level - height[i]
                    height[i] = minimum_level
            if height[high] >= height[low]:
                low += 1
            
            elif height[low] > height[high]:
                high -= 1
        
        return volume
        