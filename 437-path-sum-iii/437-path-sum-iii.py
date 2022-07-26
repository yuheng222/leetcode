# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, targetSum, path):
            if not root:
                return 0
            path.append(root.val)
            path_sum, path_count = 0, 0
            for i in reversed(range(len(path))):
                path_sum += path[i]
                if path_sum == targetSum:
                    path_count += 1
            path_count += dfs(root.left, targetSum, path)
            path_count += dfs(root.right, targetSum, path)
            path.pop() # backtrack - pop the node while moving up the call stack
            return path_count
        return dfs(root, targetSum, [])