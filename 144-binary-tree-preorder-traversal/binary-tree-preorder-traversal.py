# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        stack = []

        stack.append(root)
        while(len(stack)):
            root = stack.pop()
            if(root):
                preorder.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return preorder