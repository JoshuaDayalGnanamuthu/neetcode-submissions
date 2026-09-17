class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict, Counter

        if not t or len(s) < len(t):
            return ""

        frequency = Counter(t)
        counter = Counter()

        left = 0
        string = ""
        
        for right in range(0, len(s)):
            counter[s[right]] += 1

            for key in frequency:
                if(counter.get(key, 0) - frequency[key] < 0):
                    break
            else:
                while ((counter[s[left]] - 1) - frequency.get(s[left], 0) >= 0 ):
                   counter[s[left]] -= 1
                   left += 1
                current_string = s[left: right + 1]
                if string == "":
                    string = current_string
                elif (len(current_string) < len(string)):
                    string = current_string


        return string
        