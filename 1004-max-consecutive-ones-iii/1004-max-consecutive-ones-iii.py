class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, longest, max_ones_count = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 1:
                max_ones_count += 1
            if r - l + 1 - max_ones_count > k:
                if nums[l] == 1:
                    max_ones_count -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
        