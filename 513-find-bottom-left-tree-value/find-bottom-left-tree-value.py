# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        max_l = -1

        def find(root, lev, max_l):
            if not root:
                return
            
            if lev > max_l[0]:
                max_l[0] = lev
                self.ans = root.val
            
            find(root.left, lev+1, max_l)
            find(root.right, lev+1, max_l)
        
        find(root, 0, [-1])

        return self.ans