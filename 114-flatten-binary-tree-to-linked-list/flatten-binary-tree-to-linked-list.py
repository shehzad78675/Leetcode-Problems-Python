# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        stack = []
        stack.append(root)
        temp = root

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
            if stack:
                temp.right = stack[-1]
                temp = temp.right
            node.left = None