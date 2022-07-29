class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, find_max_index):
            target_index = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else: # if target is found
                    target_index = mid
                    if find_max_index: # if find max index flag is set to true, look to the right
                        l = mid + 1
                    else:
                        r = mid - 1
            return target_index
        res = [-1, -1]
        res[0] = binary_search(nums, target, False)
        if res[0] != -1:
            res[1] = binary_search(nums, target, True)
        return res
                        
                        
    
        