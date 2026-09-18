class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity O(m * N), Space Complexity O(m)

        from collections import defaultdict

        anagrams = defaultdict(list)

        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - 97] += 1
            anagrams[tuple(chars)].append(string)
        
        return [values for values in anagrams.values()]






        