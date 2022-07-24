class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = len(nums)
        for i, val in enumerate(nums):
            missing_num ^= i ^ val
        return missing_num