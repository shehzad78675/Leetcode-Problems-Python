# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack1 = []
        stack2 = []

        stack1.append(root)
        while(stack1):
            root = stack1.pop()
            if not root:
                continue
            stack2.append(root.val)
            stack1.append(root.left)
            stack1.append(root.right)

        res = []
        while(stack2):
            res.append(stack2.pop())
        
        return res