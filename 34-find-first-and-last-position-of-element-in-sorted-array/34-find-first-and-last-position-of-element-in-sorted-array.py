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
                else:
                    target_index = mid # if target is found
                    if find_max_index: # find the max index of the found number
                        l = mid + 1
                    else:
                        r = mid - 1 # else find the min index of the found number
            return target_index
                        
        result = [-1, -1]
        result[0] = binary_search(nums, target, False)
        if result[0] != -1: # if target found, then run binary search again to locate 
            result[1] = binary_search(nums, target, True)
        return result
    
        