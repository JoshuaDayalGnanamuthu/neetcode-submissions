class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: empty node, or we found either p or q
        if not root or root == p or root == q:
            return root
        
        # Search in the left and right subtrees (postorder)
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return non-None, root is the split point (LCA)
        if left and right:
            return root
        
        # Otherwise, pass up whichever side found something (or None if neither did)
        return left if left else right