class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        
        from collections import Counter
        
        max_length = 1

        left = 0

        frequencies = Counter()
        frequencies[s[left]] += 1

        for right in range(1, len(s)):
            frequencies[s[right]] += 1

            if (frequencies[s[right]] > 1):
                while(frequencies[s[right]] > 1):
                    frequencies[s[left]] -= 1
                    left += 1
            else:
                current_length = right - left + 1
                max_length = max(current_length, max_length)
        
        return max_length



        