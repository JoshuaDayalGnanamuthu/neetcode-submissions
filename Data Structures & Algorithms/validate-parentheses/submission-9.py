class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'(': ')', '{':'}', '[':']'}

        stack = []

        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if not stack or hash_map[stack.pop()] != char:
                    return False

        return not stack
        
                    