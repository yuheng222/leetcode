class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            # if complement is not found in dict, add current number to dict
            if complement not in sum_dict:
                sum_dict[num] = i
            # Else, return the index of the current number and the index of its complement
            else:
                return[i, sum_dict[complement]]