# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def bst(preorder, max_v, ind):
            if ind[0] == len(preorder) or max_v < preorder[ind[0]]:
                return None
            
            root = TreeNode(preorder[ind[0]])
            ind[0] += 1

            root.left = bst(preorder, root.val, ind)
            root.right = bst(preorder, max_v, ind)

            return root
        
        return bst(preorder, float("inf"), [0])