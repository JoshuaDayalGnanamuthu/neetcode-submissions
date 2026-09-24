class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        frequencies = Counter(s1)
        counter = Counter()

        left = 0

        counter[s2[left]] += 1

        for right in range(1, len(s2)):
            if (counter == frequencies):
                return True

            counter[s2[right]] += 1

            if (counter == frequencies):
                return True
            
            else:
                while (left < right and counter.get(s2[left]) != frequencies.get(s2[left], 0)):
                    if (counter.get(s2[left], 0) > frequencies.get(s2[left], 0)):
                        counter[s2[left]] -= 1
                        left += 1
                    else:
                        break
        
        return counter == frequencies
