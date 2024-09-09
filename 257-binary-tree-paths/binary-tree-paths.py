# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def treePaths(root, path):
            if not root:
                return
            path += str(root.val)
            if root.left is None and root.right is None:
                paths.append(path)
                return

            path += '->'

            treePaths(root.left, path)
            treePaths(root.right, path)
        
        treePaths(root, "")

        return paths