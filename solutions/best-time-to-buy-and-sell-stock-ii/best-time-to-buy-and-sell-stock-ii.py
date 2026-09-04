class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            buy, sell = prices[i], prices[i+1]
            if buy < sell:
                profit += sell - buy
        return profit