class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, curr = 0, 0
        r = len(nums) - 1
        while curr <= r:
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l] # swap left and curr
                l += 1 # shift both the curr and left pointers
                curr += 1
            elif nums[curr] == 2:
                nums[r], nums[curr] = nums[curr], nums[r]
                r -= 1 # shift the right pointer
            else:
                curr += 1 # else if curr = 1, just increment curr without swapping
        