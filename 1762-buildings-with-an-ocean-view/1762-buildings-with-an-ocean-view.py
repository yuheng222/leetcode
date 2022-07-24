class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        res = []
        for i in reversed(range(len(heights))):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        return reversed(res)