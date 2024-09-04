# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, min, max):
            if root is None:
                return True
            
            if root.val <= min or root.val >= max:
                return False
            
            left = valid(root.left, min, root.val)
            right = valid(root.right, root.val, max)

            return left and right
        
        min = float("-inf")
        max = float("inf")

        return valid(root, min, max)