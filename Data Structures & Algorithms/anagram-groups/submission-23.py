class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        hash = defaultdict(list) # create a dict where all the values are lists by defaultdict


        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - 97] += 1
            key = ""
            for i in chars:
                key += str(i) + ","
            
            hash[key].append(string)
        
        return [value for _, value in hash.items()]
            





        