from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        heap = []
        for num, freq in freq_map.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res
            