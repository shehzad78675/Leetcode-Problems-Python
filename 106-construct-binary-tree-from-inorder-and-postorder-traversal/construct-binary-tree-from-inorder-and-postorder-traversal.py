# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder, si, ei, postorder, sp, ep):
            if si > ei or sp > ep:
                return None

            root = TreeNode(postorder[ep])

            root_index = inorder.index(postorder[ep])
            nums_left = root_index - si

            root.left = build(inorder, si, root_index - 1, postorder, sp, sp + nums_left - 1)
            root.right = build(inorder, root_index + 1, ei, postorder, sp + nums_left, ep - 1)

            return root

        return build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

