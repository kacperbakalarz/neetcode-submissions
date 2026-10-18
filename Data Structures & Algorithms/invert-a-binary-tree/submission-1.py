# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return;
            dfs(node.left)
            dfs(node.right)
            
            left_sub = None
            right_sub = None
            
            if node.left is not None:
                left_sub = node.left
            if node.right is not None:
                right_sub = node.right

            node.left = right_sub
            node.right = left_sub
        dfs(root)
        return root