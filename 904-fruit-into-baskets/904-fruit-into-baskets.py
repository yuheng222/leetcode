class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruits_map = {}
        max_fruits = 0
        l = 0
        for r in range(len(fruits)):
            fruits_map[fruits[r]] = 1 + fruits_map.get(fruits[r], 0)
            while len(fruits_map) > 2:
                fruits_map[fruits[l]] -= 1
                if fruits_map[fruits[l]] == 0:
                    del fruits_map[fruits[l]]
                l += 1
            max_fruits = max(max_fruits, r - l + 1)
        return max_fruits
    