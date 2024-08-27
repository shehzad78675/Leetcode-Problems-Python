# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def findMax(root):
            if(not root):
                return 0
            
            ld = findMax(root.left)
            rd = findMax(root.right)

            self.res = max(self.res, ld + rd)

            return max(ld, rd) + 1

        findMax(root)

        return self.res