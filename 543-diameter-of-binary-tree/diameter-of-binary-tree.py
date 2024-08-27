# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findMax(root, res):
            if(not root):
                return 0
            
            ld = findMax(root.left, res)
            rd = findMax(root.right, res)

            res[0] = max(res[0], ld + rd)

            return max(ld, rd) + 1

        res = [0]
        findMax(root, res)

        return res[0]

