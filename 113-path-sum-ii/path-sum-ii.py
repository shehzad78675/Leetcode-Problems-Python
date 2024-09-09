# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def hasPathSum(root, target, path):
            if not root:
                return
            
            path.append(root.val)
            if root.val - target == 0 and root.left is None and root.right is None:
                paths.append(list(path))
                path.pop()
                return

            left = hasPathSum(root.left, target - root.val, path)
            right = hasPathSum(root.right, target - root.val, path)

            path.pop()        

        path = []
        hasPathSum(root, targetSum, path)
        return paths