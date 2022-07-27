class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == arr[mid + k]:
                if x > arr[mid]:
                    l = mid + 1
                else:
                    r = mid
            elif abs(x - arr[mid]) > abs(x - arr[mid + k]):
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]