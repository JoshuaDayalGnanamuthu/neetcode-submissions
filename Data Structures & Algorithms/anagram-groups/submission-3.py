from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        valid_anagrams = defaultdict(list)
        for i in strs:
            sorted_word = "".join(sorted(i))
            valid_anagrams[sorted_word].append(i)
        
        return [x for x in valid_anagrams.values()]

        