class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum, totalSum = 0, sum(nums)
        for i in range(n):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1