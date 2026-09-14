from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def encoding(string :str) -> tuple:
            chars = [0 for i in range(26)]
            for i in range(len(string)):
                chars[ord(string[i]) - 97]+=1
            
            return tuple(chars)

        map = defaultdict(list)

        for string in strs:
            map[encoding(string)].append(string)
        
        results = []

        for key, values in map.items():
            results.append(values)
        
        return results

        