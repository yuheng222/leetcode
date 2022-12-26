class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            # add the result for the current permutation
            res.extend(perms)
            # backtrack, add back the num after removing it
            nums.append(n)
        return res