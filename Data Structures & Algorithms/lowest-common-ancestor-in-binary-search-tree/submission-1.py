# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = []

        from collections import deque

        queue = deque([root])

        while queue:
            current = queue.pop()
            sub_queue = deque([current])
            p_seen = False; q_seen = False
            while sub_queue:
                current_sub_node = sub_queue.pop()
                if (current_sub_node == p):
                    p_seen = True
                if current_sub_node == q:
                    q_seen = True
                
                if current_sub_node.left:
                    sub_queue.append(current_sub_node.left)
                
                if current_sub_node.right:
                    sub_queue.append(current_sub_node.right)
            if p_seen and q_seen:
                ancestors.append(current)
            
            if current.left:
                    queue.append(current.left)
                
            if current.right:
                    queue.append(current.right)
        
        return ancestors[-1]


        