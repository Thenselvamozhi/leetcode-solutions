class Solution(object):
    def runningSum(self, nums):
        sum = 0
        ans = []
        for i in nums:
            sum += i
            ans.append(sum)
        return ans