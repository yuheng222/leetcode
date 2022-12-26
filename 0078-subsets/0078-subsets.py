class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # left branch, we choose to include the number
            subset.append(nums[i])
            dfs(i + 1)
            # backtracking -> right branch, we choose to exclude the number
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res