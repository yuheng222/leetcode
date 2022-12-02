class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                return True
        return False