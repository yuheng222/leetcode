class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        arr_sum = 0
        for num in nums:
            arr_sum += num
        return expected_sum - arr_sum