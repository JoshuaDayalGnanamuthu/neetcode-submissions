class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while high > low:
            sum1 = numbers[low] + numbers[high]
            if sum1 == target:
                return [low + 1, high + 1]
            if sum1 > target:
                high -= 1
            if sum1 < target:
                low += 1

        