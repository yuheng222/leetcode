# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(root, arr, arr_idx):
            if not root:
                return False
            arr_len = len(arr)
            if arr_idx > arr_len - 1 or root.val != arr[arr_idx]:
                return False
            # if current node is a leaf, and it is at the end of the seq, then a path is found
            if not root.left and not root.right and arr_idx == arr_len - 1:
                return True
            return dfs(root.left, arr, arr_idx + 1) or dfs(root.right, arr, arr_idx + 1)
        if not root:
            return len(arr) == 0
        return dfs(root, arr, 0)
            