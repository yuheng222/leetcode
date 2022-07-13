class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        running_sum = 0
        for n in nums:
            running_sum += n
            res.append(running_sum)
        return res