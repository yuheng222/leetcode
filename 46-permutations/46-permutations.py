from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        res = []
        permutations = deque()
        permutations.append([])
        for num in nums:
            # take all existing permutations and add current number to create new permutations
            n = len(permutations)
            for _ in range(n):
                old_permutation = permutations.popleft()
                for j in range(len(old_permutation)+1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(j, num)
                    if len(new_permutation) == nums_length:
                        res.append(new_permutation)
                    else:
                        permutations.append(new_permutation)
        return res
        