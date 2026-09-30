# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

            
        level_order = []
        
        queue = deque([root])
        num_nodes = 1
        level = 1

        while queue:
            nodes = []
            level = num_nodes
            num_nodes = 0
            for _ in range(level):
                currrent = queue.popleft()
                nodes.append(currrent.val)
                if currrent.left:
                    queue.append(currrent.left)
                    num_nodes += 1
                if currrent.right:
                    queue.append(currrent.right)
                    num_nodes += 1

            level_order.append(nodes)
        
        return level_order
