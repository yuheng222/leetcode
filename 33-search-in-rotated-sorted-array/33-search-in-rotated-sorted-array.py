class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid  
            # check if left sorted portion
            if nums[l] <= nums[mid]: # left portion
                if target > nums[mid] or target < nums[l]: # search right
                    l = mid + 1
                else: # search right
                    r = mid - 1
            else: # right
                if target < nums[mid] or target > nums[r]: # search left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        