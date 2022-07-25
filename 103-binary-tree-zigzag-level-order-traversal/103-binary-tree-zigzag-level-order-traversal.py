# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return None
        queue = collections.deque()
        queue.append(root)
        left_to_right = True
        while queue:
            level_size = len(queue)
            current_level = collections.deque()
            for i in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_level)
            left_to_right = not left_to_right
        return res
                    