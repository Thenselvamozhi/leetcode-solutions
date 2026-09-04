class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            buy = prices[i]
            sell = prices[i+1]
            if buy < sell:
                profit += sell - buy
        return profit