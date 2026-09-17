class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_count = 1
        left = 0
        seen = set()
        seen.add(s[left])

        for right in range(1, len(s)):
            if (s[right] in seen):
                while(s[left] != s[right]):
                    seen.remove(s[left])
                    left += 1
                left += 1
                seen.add(s[right])
            else:
                seen.add(s[right])
                max_count = max(max_count, right - left + 1)
        
        return max_count