class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        while l <= r:
            left_num = nums[l] ** 2
            right_num = nums[r] ** 2
            if left_num > right_num:
                res[i] = left_num
                l += 1
            else:
                res[i] = right_num
                r -= 1
            i -= 1
        return res
            
            
        
        
        