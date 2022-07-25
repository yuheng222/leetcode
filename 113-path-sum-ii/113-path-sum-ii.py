# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def find_paths(currentNode, targetSum, currentPath, allPaths):
            if not currentNode:
                return None
            currentPath.append(currentNode.val)
            if currentNode.val == targetSum and currentNode.left is None and currentNode.right is None:
                allPaths.append(list(currentPath))
            else:
                find_paths(currentNode.left, targetSum - currentNode.val, currentPath, allPaths)
                find_paths(currentNode.right, targetSum - currentNode.val, currentPath, allPaths)
            currentPath.pop()
        allPaths = []
        find_paths(root, targetSum, [], allPaths)
        return allPaths