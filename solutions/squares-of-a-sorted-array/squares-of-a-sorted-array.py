class Solution(object):
    def sortedSquares(self, nums):
        ans = [0]*len(nums)
        left, right = 0, len(nums)-1
        index = len(nums)-1
        while left <= right:
            if abs(nums[left]) >= nums[right]:
                ans[index] = nums[left] ** 2
                left += 1
            else:
                ans[index] = nums[right] ** 2
                right -= 1
            index -= 1
        return ans