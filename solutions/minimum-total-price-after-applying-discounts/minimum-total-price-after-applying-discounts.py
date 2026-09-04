class Solution(object):
    def minPrice(self, prices, discounts):
        ans = 0
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        for i in range(len(prices)):
            if i < len(discounts):
                ans += prices[i] * (100 - discounts[i]) / 100.0
            else:
                ans += prices[i]
        return ans