class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_so_far = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_so_far:
                min_so_far = price
            elif price - min_so_far > max_profit:
                max_profit = price - min_so_far
        return max_profit
            