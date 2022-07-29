class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = float('-inf')
        for i in reversed(range(len(heights))):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        return reversed(res)