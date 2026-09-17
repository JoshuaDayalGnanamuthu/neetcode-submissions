class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0

        for right in range(1, len(prices)):
            if (prices[left] > prices[right]):
                left = right
            else:
                current_profit = prices[right] - prices[left]
                if (current_profit > max_profit):
                    max_profit = current_profit
            
        
        return max_profit


