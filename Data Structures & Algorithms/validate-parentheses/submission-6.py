class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'(': ')', '{':'}', '[':']'}

        stack = []

        for i in s:
            if i in hash_map.keys():
                stack.append(i)
            else:
                if (not stack or i != hash_map[stack[-1]]):
                    return False
                else:
                    stack.pop()
        
        if len(stack): return False

        return True
