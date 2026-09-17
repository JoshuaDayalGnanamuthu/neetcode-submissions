class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        if not s:
            return 0

        max_count = 1
        max_frequency = 1
        left = 0

        counter = defaultdict(int)
        counter[s[0]] += 1

        for right in range(1, len(s)):
            counter[s[right]] += 1

            max_frequency = max(max_frequency, counter[s[right]])

            while (left < right and (right - left + 1) - max_frequency > k):
                counter[s[left]]-= 1
                left += 1

                
            current_count = right - left + 1
            if (current_count > max_count):
                    max_count = current_count
        
        return max_count

            
        