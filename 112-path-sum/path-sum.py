# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root, sum):
            if not root:
                return False
            
            if sum + root.val == targetSum and not root.left and not root.right:
                return True

            left = path(root.left, sum + root.val)
            right = path(root.right, sum + root.val)

            return left or right
        
        return path(root, 0)
            
            