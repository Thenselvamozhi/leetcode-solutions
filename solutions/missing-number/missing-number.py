class Solution(object):
    def missingNumber(self, nums):
        currentSum = 0
        for i in nums:
            currentSum += i
        n = len(nums)
        expectedSum = n*(n+1) / 2
        return expectedSum - currentSum