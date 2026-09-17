class Solution(object):
    def pivotIndex(self, nums):
        n, total = len(nums), sum(nums)
        leftSum = 0
        for i in range(n):
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1