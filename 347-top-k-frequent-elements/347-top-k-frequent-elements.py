from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, freq in count.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        for tup in heap:
            res.append(tup[1])
        return res