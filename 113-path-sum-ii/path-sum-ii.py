# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def treePaths(root, target, path):
            if not root:
                return

            path.append(root.val)
            if not root.left and not root.right:
                paths.append(list(path))
                path.pop()
                return
            
            # if not root.left and not root.right and root.val == target:
               

            treePaths(root.left, target - root.val, path)
            treePaths(root.right, target - root.val, path)

            path.pop()

        path = []
        treePaths(root, targetSum, path)

        new_paths = []

        for i in range(len(paths)):
            sum = 0
            for j in range(len(paths[i])):
                sum += paths[i][j]
            
            if sum == targetSum:
                new_paths.append(paths[i])
        return new_paths