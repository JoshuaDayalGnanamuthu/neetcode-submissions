from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for string in strs:
            map["".join(sorted(string))].append(string)
        
        results = []

        for key, values in map.items():
            results.append(values)
        
        return results

        