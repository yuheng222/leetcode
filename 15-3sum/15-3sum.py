class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                num_sum = num + nums[l] + nums[r]
                if num_sum > 0:
                    r -= 1
                elif num_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                    