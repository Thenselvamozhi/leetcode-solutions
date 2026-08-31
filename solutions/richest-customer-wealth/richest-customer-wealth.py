class Solution(object):
    def maximumWealth(self, accounts):
        maximum = -1
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            maximum = max(maximum, sum)
        return maximum