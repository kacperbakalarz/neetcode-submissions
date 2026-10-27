# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tab = []
        counter = 0 
        def inOrder(node, res):
            if node is None:
                return
            inOrder(node.left, res)
            res.append(node.val)
            inOrder(node.right, res)

        inOrder(root,tab)
        #print(tab)
        return tab[k-1]
