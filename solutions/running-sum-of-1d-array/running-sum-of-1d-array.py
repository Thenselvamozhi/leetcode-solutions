class Solution(object):
    def runningSum(self, nums):
        sol = []
        sum = 0
        for i in range (len(nums)):
            sum += nums[i]
            sol.append(sum)
        return sol