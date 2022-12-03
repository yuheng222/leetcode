class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] not in complement_map:
                complement_map[complement] = i
            else:
                return [complement_map[nums[i]], i]
        return []
        