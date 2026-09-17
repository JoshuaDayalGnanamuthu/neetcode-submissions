class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict, Counter

        if not t or len(s) < len(t):
            return ""

        frequency = Counter(t)
        counter = Counter()

        left = 0
        string = ""
        formed = False
        
        for right in range(len(s)):
            counter[s[right]] += 1

            if not formed:
                for key in frequency:
                    if counter[key] < frequency[key]:
                        break
                else:
                    formed = True

            if formed:
                while counter[s[left]] - 1 >= frequency.get(s[left], 0):
                    counter[s[left]] -= 1
                    left += 1

                if string == "" or right - left + 1 < len(string):
                    string = s[left:right + 1]


        return string
        