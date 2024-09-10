# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(ino, inS, inE, post, postS, postE):
            if inS > inE or postS > postE:
                return None
            
            root = TreeNode(post[postE])

            in_root = ino.index(root.val)
            nums_left = in_root - inS

            root.left = build(ino, inS, in_root - 1, post, postS, postS + nums_left-1)
            root.right = build(ino, in_root+1, inE, post, postS + nums_left, postE-1)

            return root
        
        return build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)