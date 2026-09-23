# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
    
        from collections import deque

        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 or queue2:
            current1 = queue1.popleft()
            current2 = queue2.popleft()

            if not current1 and not current2:
                continue
            elif current1.val != current2.val:
                return False
            
            if current1.left and not current2.left or current2.left and not current1.left:
                return False 
            else:
                queue1.append(current1.left)
                queue2.append(current2.left)
            
            if current1.right and not current2.right or current2.right and not current1.right:
                return False 
            
            else:
                queue1.append(current1.right)
                queue2.append(current2.right)
        
        return True
        


        