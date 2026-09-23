# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        if not root:
            return
        
        traversed_nodes = []

        queue = deque([root])

        while queue:
            current = queue.popleft()
            traversed_nodes.append(current)

            if current.left:
                queue.append(current.left)
            
            # Enqueue the right child if it exists
            if current.right:
                queue.append(current.right)


        head = traversed_nodes[0]

        for node in traversed_nodes:
            if node.left and node.right:
                temp_node = node.left
                node.left = node.right
                node.right = temp_node
            
            elif (node.left and not node.right):
                node.right = node.left
                node.left = None
            
            elif (node.right and not node.left):
                node.left = node.right
                node.right = None
            
        
        return head