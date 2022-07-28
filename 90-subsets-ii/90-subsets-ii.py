class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subsets.append([])
        end = 0
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1
            end = len(subsets) - 1
            for j in range(start, end+1):
                new_set = list(subsets[j])
                new_set.append(nums[i])
                subsets.append(new_set)
        return subsets
                
            