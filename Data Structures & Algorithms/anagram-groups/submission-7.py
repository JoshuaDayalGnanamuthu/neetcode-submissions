from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)
        
        return [x for x in anagrams.values()]


        