# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.sol = 0
        def dia(root):
            if root == None:
                return 0
            l = dia(root.left)
            r = dia(root.right)
            self.sol = max(self.sol, l + r)
            return 1 + max(l, r)
        dia(root)
        return self.sol
                
# O(N) time complexity
# O(N) SPACE complexity 
 
# 