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
            # add current node to path
            currentPath.append(currentNode.val)
            # if current node is leaf and its value is equal to targetSum, save the current path
            if currentNode.val == targetSum and not currentNode.left and not currentNode.right:
                allPaths.append(list(currentPath))
            else:
                find_paths(currentNode.left, targetSum - currentNode.val, currentPath, allPaths)
                find_paths(currentNode.right, targetSum - currentNode.val, currentPath, allPaths)
            
            # remove the current node from path to backtrack
            # the current node needs to be removed while going up the recursive call stack
            del currentPath[-1]
        all_paths = []
        find_paths(root, targetSum, [], all_paths)
        return all_paths