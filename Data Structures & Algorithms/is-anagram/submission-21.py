class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        character_array = [0] * 26

        for i in range(len(s)):
            character_array[ord(s[i]) - 97] += 1
            character_array[ord(t[i]) - 97] -= 1

        for char_count in character_array:
            if char_count:
                return False

         
        return True
        