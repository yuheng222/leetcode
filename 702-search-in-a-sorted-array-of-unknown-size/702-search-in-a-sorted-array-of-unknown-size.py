# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        
        # search boundaries
        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r <<= 1 # double the search boundary by left shifting 1 everytime
        
        # binary search
        while l <= r:
            mid = (l + r) // 2
            num = reader.get(mid)
            if target < num:
                r = mid - 1
            elif target > num:
                l = l + 1
            else:
                return mid
        return -1
            