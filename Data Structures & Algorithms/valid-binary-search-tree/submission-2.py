# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        valid = True

        def inorder(node: Optional[TreeNode]):
            nonlocal valid, prev
            if not node or not valid:
                return
            
            inorder(node.left)
            
            if not valid:
                return

            if prev is not None and node.val <= prev:
                valid = False
                return

            prev = node.val
            inorder(node.right)

        inorder(root)
        return valid
        