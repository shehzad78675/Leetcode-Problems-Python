# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        def height_of_binarytree(root):
            if root is None:
                return 0
            lh = height_of_binarytree(root.left)
            rh = height_of_binarytree(root.right)

            self.diameter = max(self.diameter, lh+rh)
            return max(lh, rh) + 1
        
        height_of_binarytree(root)

        return self.diameter
