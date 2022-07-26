from heapq import *

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        for i in sticks:
            heappush(heap, i)
        min_cost = 0
        while len(heap) > 1:
            cost = heappop(heap) + heappop(heap)
            heappush(heap, cost)
            min_cost += cost
        return min_cost
        