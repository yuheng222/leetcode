class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num not in complement_map:
                complement_map[complement] = i
            else:
                return [complement_map[num], i]
        return []
        