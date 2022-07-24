class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i] # found the duplicate if the number is equal while trying to swap
            else: # if the number is not equal to its index + 1
                i += 1
        return -1