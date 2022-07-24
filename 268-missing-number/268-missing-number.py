class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            # if number does not correspond to its index
            j = nums[i]
            if nums[i] < n and i != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1
        for i in range(n):
            if i != nums[i]:
                return i
        return n