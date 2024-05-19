# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque()
        q.append(root)

        levels = []

        while q:
            curr_size = len(q)
            cur_lvl = []
            for _ in range(curr_size):
                top = q.popleft()
                cur_lvl.append(top.val)

                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)

            levels.append(cur_lvl)
        return levels
        
        
# O(N), n being number of nodes