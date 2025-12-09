class Solution(object):
    def maximumWealth(self, accounts):
        all_total = []
        for ch in accounts:
            all_total.append(sum(ch))
        return max(all_total)