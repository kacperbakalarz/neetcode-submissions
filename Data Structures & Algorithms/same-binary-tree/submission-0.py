# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node,tab):
            
            if not node: 
                tab.append('N')
                return 
            
            dfs(node.left,tab)
            dfs(node.right,tab)
            #print(node.val)
            tab.append(node.val)
            return 

        tab1 = []
        tab2 = []

        dfs(p,tab1)
        dfs(q,tab2)
        #print(tab1,tab2)
        return tab1 == tab2
