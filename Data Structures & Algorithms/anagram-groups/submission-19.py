from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def encoding(string :str) -> str:
            chars = [0 for i in range(26)]
            for i in range(len(string)):
                chars[97 - ord(string[i])]+=1
            
            chars = [str(x) for x in chars]
            return ",".join(chars)

        map = defaultdict(list)

        for string in strs:
            map[encoding(string)].append(string)
        
        results = []

        for key, values in map.items():
            results.append(values)
        
        return results

        