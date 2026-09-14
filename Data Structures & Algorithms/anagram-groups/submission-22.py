from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for string in strs:
            chars = [0] * 26
            for i in range(len(string)):
                chars[ord(string[i]) - 97]+=1
            map[tuple(chars)].append(string)
        
        results = []

        for key, values in map.items():
            results.append(values)
        
        return results

        