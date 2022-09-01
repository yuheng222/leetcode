class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            max_profit = max(max_profit, max(prices[r] - prices[l], 0))
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max_profit
        