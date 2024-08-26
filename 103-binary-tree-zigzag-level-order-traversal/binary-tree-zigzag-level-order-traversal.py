# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
            
        queue = deque()
        level_order = []

        level = 1
        queue.append(root)

        while queue:
            in_list = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                in_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level%2 == 0:
                level_order.append(in_list[::-1])
            else:
                level_order.append(in_list)
            level += 1
        return level_order

