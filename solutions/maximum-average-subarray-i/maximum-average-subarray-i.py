class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        for i in range(k):
            maxSum += nums[i]
        maxAvg = maxSum/k
        for i in range(k, len(nums)):
            maxSum += nums[i] - nums[i-k]
            maxAvg = max(maxAvg, maxSum/k)
        return maxAvg