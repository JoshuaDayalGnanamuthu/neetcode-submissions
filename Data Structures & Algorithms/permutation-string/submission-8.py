class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        from collections import Counter

        frequencies = Counter(s1)
        counter = Counter()

        left = 0

        counter[s2[left]] += 1

        for right in range(1, len(s2)):
            if (counter == frequencies):
                return True
            
            counter[s2[right]] += 1

            if (right - left + 1 < len(s1)):
                continue
            
            else:
                if (counter == frequencies):
                    return True
                else:
                    counter[s2[left]] -= 1
                    left += 1
        
        return (counter == frequencies)

