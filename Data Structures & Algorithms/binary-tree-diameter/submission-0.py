# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def dfs(node): 
            nonlocal maxi
            if not node:
                return 0
            
            h1 = dfs(node.left)
            h2 = dfs(node.right)

            maxi = max(maxi,h1+h2)
            return max(h1,h2)+1
        
        dfs(root)
        return maxi
        
        