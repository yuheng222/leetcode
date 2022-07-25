# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)
        while root:
            res += 1
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return res
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res