class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        frequency = defaultdict(int)

        left = 0
        max_count = 1

        frequency[s[left]] += 1

        for right in range(1, len(s)):
            frequency[s[right]] += 1

            if (frequency.get(s[right]) == 1):
                current_count = right - left + 1
                if current_count > max_count:
                    max_count = current_count
            
            else:
                while (frequency.get(s[right], 0) > 1 and left < right):
                    frequency[s[left]] -= 1
                    left += 1
        
        return max_count
