# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Initialize queue with the root
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            
            # 1. Swap the children immediately (handles None values seamlessly)
            current.left, current.right = current.right, current.left
            
            # 2. Add the existing children to the queue to continue down the tree
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
        return root