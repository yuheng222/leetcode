class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res