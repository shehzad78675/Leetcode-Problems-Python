# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    val = []

    def __init__(self, root: Optional[TreeNode]):
        self.inorder(root)

    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        self.val.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        return self.val.pop(0)

    def hasNext(self) -> bool:
        if len(self.val):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()