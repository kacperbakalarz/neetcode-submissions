# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            nonlocal balance
            if balance == False:
                return 0
            if not node:
                return 0 
            h1 = dfs(node.left)  
            h2 = dfs(node.right)
            if abs(h1-h2) > 1:
                balance = False
            return max(h1,h2)+1
        balance = True
        dfs(root)
        return balance