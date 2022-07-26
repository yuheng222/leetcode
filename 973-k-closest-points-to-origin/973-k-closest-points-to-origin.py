from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate_distance(points):
            return points[0] ** 2 + points[1] ** 2
        heap = []
        for i in range(k):
            dist = -calculate_distance(points[i])
            heappush(heap, (dist, i))
        for i in range(k, len(points)):
            dist = -calculate_distance(points[i])
            if dist > heap[0][0]:
                heappushpop(heap, (dist, i))
        return [points[i] for _, i in heap]