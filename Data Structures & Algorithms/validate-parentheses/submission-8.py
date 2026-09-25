class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'(': ')', '{':'}', '[':']'}

        stack = []

        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if stack:
                    if hash_map[stack[-1]] == char:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if not len(stack):
            return True
        else:
            return False