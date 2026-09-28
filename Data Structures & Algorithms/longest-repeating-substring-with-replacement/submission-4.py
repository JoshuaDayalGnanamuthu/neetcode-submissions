class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter

        left = 0
        counter = Counter()

        counter[s[0]] += 1

        max_length = 1
        max_frequency = 1

        for right in range(1, len(s)):
            counter[s[right]] += 1

            max_frequency = max(values for values in counter.values())

            while ((right - left + 1) - max_frequency > k):
                counter[s[left]] -= 1
                left += 1
            
            length = (right - left + 1)
            max_length = max(max_length, length)
        
        return max_length


        

            
        