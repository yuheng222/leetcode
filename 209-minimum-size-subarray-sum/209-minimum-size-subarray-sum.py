class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_subarr = float('inf')
        subarr_sum = 0
        l = 0
        for r in range(len(nums)):
            subarr_sum += nums[r]
            while subarr_sum >= target:
                min_subarr = min(min_subarr, r - l + 1)
                subarr_sum -= nums[l]
                l += 1
        if min_subarr == float('inf'):
            return 0
        return min_subarr
        
                