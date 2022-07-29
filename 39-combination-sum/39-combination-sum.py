class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            # if we found our target sum, then append the cur subset to result
            if total == target:
                res.append(list(cur)) # return a copy of the current list since cur keeps changing
                return
            if i > len(candidates) - 1 or total > target: # base case
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i]) # include the candidate
            cur.pop() # backtrack
            dfs(i + 1, cur, total) # not including occurences of i
        dfs(0, [], 0)
        return res