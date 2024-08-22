# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        queue = [root]
        level_order = []
        level = 1
        while queue:
            in_list = []
            for i in range(len(queue)):
                node = queue.pop(0)
                in_list.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            
            if(level%2 == 0):
                level_order.append(in_list[::-1])
            else:
                level_order.append(in_list)
            level += 1
        
        return level_order