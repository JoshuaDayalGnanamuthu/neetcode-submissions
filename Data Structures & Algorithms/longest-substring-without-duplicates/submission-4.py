class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            # Shrink the window until the duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_count = max(max_count, right - left + 1)

        return max_count