from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, freq in count.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        while heap:
            res.append(heappop(heap)[1])
        return res