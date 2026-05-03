class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(word1, word2):
            if len(word1) != len(word2): return False
            letters = [0] * 26
            for i in range(len(word1)):
                letters[97 - ord(word1[i])] += 1
                letters[97 - ord(word2[i])] -= 1
            for i in letters:
                if i != 0: return False
            return True

        output = []

        while strs:
            i = strs.pop(0)
            l1 = [i]
            for index, j in enumerate(strs): 
                if isAnagram(i, j):
                    l1.append(j)
            for k in l1[1:]:
                strs.remove(k)
            output.append(l1)
        
        return output

        