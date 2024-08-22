# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
            
        stack1 = []
        stack2 = []
        post = []

        stack1.append(root)
        while(stack1):
            root = stack1.pop()
            stack2.append(root.val)
            if(root.left):
                stack1.append(root.left)
            if(root.right):
                stack1.append(root.right)
        
        while(stack2):
            num = stack2.pop()
            post.append(num)
        return post