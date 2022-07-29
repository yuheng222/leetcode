class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i > len(nums) - 1:
                res.append(list(subset))
                return
            
            # left branch that includes the element
            subset.append(nums[i])
            dfs(i + 1)
            
            # right branch that excludes the element
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res
            