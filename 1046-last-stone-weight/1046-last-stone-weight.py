from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        for stone in stones:
            heappush(heap, -stone)
        while len(heap) > 1:
            stone1 = heappop(heap)
            stone2 = heappop(heap)
            if stone1 != stone2:
                heappush(heap, -(stone2-stone1))
        return -heap[0] if heap else 0
