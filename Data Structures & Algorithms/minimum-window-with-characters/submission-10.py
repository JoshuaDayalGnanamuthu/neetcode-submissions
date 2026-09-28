class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict, Counter

        if len(t) > len(s):
            return ""

        matched = 0

        counter = Counter()
        left = 0
        min_string = ""
        seen = set()
        frequency = Counter(t)

        for right in range(len(s)):
            counter[s[right]] += 1

            if frequency.get(s[right]):
                if counter[s[right]] >= frequency[s[right]] and s[right] not in seen:
                    seen.add(s[right])
                    matched += 1

            if (matched == len(frequency)):
                while (counter.get(s[left], 0) - 1 >= frequency.get(s[left], 0)):
                    counter[s[left]] -= 1
                    left += 1
                
                string = s[left: right + 1]
                min_string = string if (len(string) < len(min_string) or not len(min_string)) else min_string
        
        return min_string

