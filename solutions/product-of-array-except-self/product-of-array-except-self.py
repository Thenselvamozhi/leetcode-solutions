class Solution(object):
    def productExceptSelf(self, nums):
        ans = [1]*len(nums)
        suffix = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix
        return ans