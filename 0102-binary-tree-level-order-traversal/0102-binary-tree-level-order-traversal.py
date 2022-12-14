# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque()
        res.append([root.val])
        queue.append(root)
        while queue:
            level_nodes = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level_nodes.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level_nodes.append(node.right.val)
                    queue.append(node.right)
            if level_nodes:
                res.append(level_nodes)
        return res
            
