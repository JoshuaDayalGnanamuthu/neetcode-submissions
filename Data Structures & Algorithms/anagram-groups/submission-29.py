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
        
        return [value for _, value in anagrams.items()]






        