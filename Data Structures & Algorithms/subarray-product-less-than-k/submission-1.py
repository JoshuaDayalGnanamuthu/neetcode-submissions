class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        current_prod = 1
        total_count = 0

        for right in range(len(nums)):
            current_prod *= nums[right]

            # Shrink from the left until product is strictly less than k
            while current_prod >= k and left <= right:
                current_prod //= nums[left]
                left += 1

            # All subarrays ending at `right` starting from `left..right` are valid
            total_count += right - left + 1

        return total_count