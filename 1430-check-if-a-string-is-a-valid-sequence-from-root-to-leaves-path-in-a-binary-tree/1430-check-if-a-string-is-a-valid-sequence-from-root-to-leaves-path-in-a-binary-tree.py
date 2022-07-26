# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(root, arr, node_idx):
            if not root:
                return False
            if node_idx > len(arr) - 1 or root.val != arr[node_idx]:
                return False
            if not root.left and not root.right and node_idx == len(arr) - 1:
                return True
            return dfs(root.left, arr, node_idx + 1) or dfs(root.right, arr, node_idx + 1)
        return dfs(root, arr, 0)