class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        def search_pair(nums, target_sum, first):
            count = 0
            left, right = first + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target_sum:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count
            
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            count += search_pair(nums, target - nums[i], i)
        return count