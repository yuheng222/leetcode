from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        for stone in stones:
            heappush(heap, -stone)
        while len(heap) > 1:
            num1 = heappop(heap)
            num2 = heappop(heap)
            if num1 != num2:
                heappush(heap, -abs(num2 - num1))
        return -heap[0] if heap else 0