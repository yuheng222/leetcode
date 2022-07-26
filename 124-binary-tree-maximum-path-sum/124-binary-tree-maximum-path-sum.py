# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            left_path = max(dfs(root.left), 0)
            right_path = max(dfs(root.right), 0)
            current_max_path = left_path +  right_path + root.val
            max_sum = max(max_sum, current_max_path)
            return max(left_path, right_path) + root.val
        dfs(root)
        return max_sum